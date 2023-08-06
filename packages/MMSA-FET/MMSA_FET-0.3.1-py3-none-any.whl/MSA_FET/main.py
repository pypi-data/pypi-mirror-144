import json
import logging
import multiprocessing
import os
import os.path as osp
import pickle
import shutil
import time
from glob import glob
from logging.handlers import RotatingFileHandler
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from .ASD import run_ASD
from .dataloader import FET_Dataset
from .extractors import *
from .utils import *


class FeatureExtractionTool(object):
    """
    Feature Extraction Tool for Multimodal Sentiment Analysis tasks.

    Parameters:
        config: 
            Python dictionary or path to a JSON file.
        dataset_root_dir: 
            Path to dataset root directory. Used when extracting dataset features.
        tmp_dir: 
            Temporary directory path. Default: '~/.MSA-FET/tmp'.
        log_dir: 
            Log directory path. Default: '~/.MSA-FET/log'.
        verbose: 
            Verbose level of stdout. 0 for error, 1 for info, 2 for debug. Default: 1.

    TODOs:
        1. Support VGGFace2 or DenseFace
        2. Add option to pad zeros instead of discard the frame when no human faces are detected.
        3. Add csv/dataframe output format.
        4. Support specifying existing feature files, modify only some of the modalities.
        5. Fix memory leak. Write to pkl file every batch.
        6. Based on 5, implement resume function.
    """

    def __init__(
        self,
        config,
        dataset_root_dir=None,
        tmp_dir=osp.join(Path.home(), '.MMSA-FET/tmp'),
        log_dir=osp.join(Path.home(), '.MMSA-FET/log'),
        verbose=1
    ):
        if type(config) == dict:
            self.config = config
        elif type(config) == str:
            if osp.isfile(config):
                with open(config, 'r') as f:
                    self.config = json.load(f)
            elif osp.isfile(name := osp.join(osp.dirname(__file__), 'example_configs', config + '.json')):
                with open(name, 'r') as f:
                    self.config = json.load(f)
            elif osp.isfile(name := osp.join(osp.dirname(__file__), 'example_configs', config)):
                with open(name, 'r') as f:
                    self.config = json.load(f)
            else:
                raise ValueError(f"Config file {config} does not exist.")
        else:
            raise ValueError("Invalid config type.")
        self.tmp_dir = tmp_dir
        self.log_dir = log_dir
        self.dataset_root_dir = dataset_root_dir
        self.verbose = verbose

        if not osp.isdir(self.tmp_dir):
            Path(self.tmp_dir).mkdir(parents=True, exist_ok=True)
        if not osp.isdir(self.log_dir):
            Path(self.log_dir).mkdir(parents=True, exist_ok=True)
            
        self.logger = logging.getLogger("MMSA-FET")
        if self.verbose == 1:
            self.__set_logger(logging.INFO)
        elif self.verbose == 0:
            self.__set_logger(logging.ERROR)
        elif self.verbose == 2:
            self.__set_logger(logging.DEBUG)
        else:
            raise ValueError(f"Invalid verbose level '{self.verbose}'.")
        
        self.logger.info("")
        self.logger.info("========================== MMSA-FET Started ==========================")
        self.logger.info(f"Temporary directory: {self.tmp_dir}")
        self.logger.info(f"Log file: '{osp.join(self.log_dir, 'MMSA-FET.log')}'")
        # self.logger.info(f"Config file: '{self.config_file}'")
        self.logger.info(f"Config: {self.config}")

        self.video_extractor, self.audio_extractor, self.text_extractor = None, None, None
        

    def __set_logger(self, stream_level):
        self.logger.setLevel(logging.DEBUG)

        fh = RotatingFileHandler(osp.join(self.log_dir, 'MSA-FET.log'), maxBytes=2e7, backupCount=5)
        fh_formatter = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s] - %(message)s')
        fh.setFormatter(fh_formatter)
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(stream_level)
        ch_formatter = logging.Formatter('%(name)s - %(message)s')
        ch.setFormatter(ch_formatter)
        self.logger.addHandler(ch)

    def __init_extractors(self):
        if 'audio' in self.config and self.audio_extractor is None:
            # self.logger.info(f"Initializing audio feature extractor...")
            audio_cfg = self.config['audio']
            extractor_name = audio_cfg['tool']
            self.audio_extractor = AUDIO_EXTRACTOR_MAP[extractor_name](audio_cfg, self.logger)
        if 'video' in self.config and self.video_extractor is None:
            # self.logger.info(f"Initializing video feature extractor...")
            video_cfg = self.config['video']
            extractor_name = video_cfg['tool']
            self.video_extractor = VIDEO_EXTRACTOR_MAP[extractor_name](video_cfg, self.logger)
        if 'text' in self.config and self.text_extractor is None:
            # self.logger.info(f"Initializing text feature extractor...")
            text_cfg = self.config['text']
            extractor_name = text_cfg['model']
            self.text_extractor = TEXT_EXTRACTOR_MAP[extractor_name](text_cfg, self.logger)
    
    def __audio_extract_single(self, in_file, keep_tmp_file=False):
        # extract audio from video file
        # extension = get_codec_name(in_file, 'audio')
        tmp_audio_file = osp.join(self.tmp_dir, 'tmp_audio.wav')
        ffmpeg_extract(in_file, tmp_audio_file, mode='audio')
        
        # extract audio features
        audio_result = self.audio_extractor.extract(tmp_audio_file)
        # delete tmp audio file
        if not keep_tmp_file:
            os.remove(tmp_audio_file)
        return audio_result

    def __video_extract_single(self, in_file, keep_tmp_file=False):
        # extract images from video
        fps = self.config['video']['fps']
        if 'multiFace' in self.config['video'] and self.config['video']['multiFace']['enable'] == True:
            # enable Active Speaker Detection
            run_ASD(in_file, self.tmp_dir, fps, self.config['video']['multiFace'])
        else:
            ffmpeg_extract(in_file, self.tmp_dir, mode='image', fps=fps)

        # extract video features
        name = 'video_' + Path(in_file).stem
        video_result = self.video_extractor.extract(self.tmp_dir, name, tool_output=self.verbose>0)
        # delete tmp images
        if not keep_tmp_file:
            for image_path in glob(osp.join(self.tmp_dir, '*.bmp')):
                os.remove(image_path)
            for image_path in glob(osp.join(self.tmp_dir, '*.jpg')):
                os.remove(image_path)
        return video_result

    def __text_extract_single(self, in_file):
        text = self.text_extractor.load_text(in_file)
        text_result = self.text_extractor.extract(text)
        # text_tokens = self.text_extractor.tokenize(text)
        return text_result

    def __read_label_file(self, dataset_name, dataset_root_dir, dataset_dir):
        # Locate and read label.csv file
        assert dataset_name is not None or dataset_dir is not None, "Either 'dataset_name' or 'dataset_dir' must be specified."
        if dataset_dir: # Use dataset_dir
            dataset_dir = osp.normpath(dataset_dir) # normalize path, remove trailing slash so that osp.basename function works correctly
            dataset_name = osp.basename(dataset_dir)
            if not osp.exists(dataset_dir):
                raise RuntimeError(f"Dataset directory '{self.dataset_dir}' does not exist.")
            if not osp.exists(osp.join(dataset_dir, 'label.csv')):
                raise RuntimeError(f"Label file '{dataset_dir}/label.csv' does not exist.")
            label_df = pd.read_csv(
                osp.join(dataset_dir, 'label.csv'),
                dtype={'clip_id': str, 'video_id': str, 'text': str}
            )
            return label_df, dataset_dir, dataset_name, None
        else: # Use dataset_name
            dataset_root_dir = dataset_root_dir if dataset_root_dir is not None else self.dataset_root_dir
            if dataset_root_dir is None:
                raise ValueError("Dataset root directory is not specified.")
            if not osp.exists(dataset_root_dir):
                raise RuntimeError(f"Dataset root directory '{dataset_root_dir}' does not exist.")
            try: # Try to locate label.csv according to global dataset config file
                with open(osp.join(self.dataset_root_dir, 'config.json'), 'r') as f:
                    dataset_config_all = json.load(f)
                dataset_config = dataset_config_all[dataset_name]
                label_file = osp.join(self.dataset_root_dir, dataset_config['label_path'])
            except: # If failed, try to locate label.csv using joined path
                label_file = osp.join(dataset_root_dir, dataset_name, 'label.csv')
            if not osp.exists(label_file):
                raise RuntimeError(f"Label file '{label_file}' does not exist.")
            label_df = pd.read_csv(
                label_file,
                dtype={'clip_id': str, 'video_id': str, 'text': str}
            )
            return label_df, osp.dirname(label_file), dataset_name, dataset_config

    def __padding(self, feature, MAX_LEN, value='zero', location='end'):
        """
        Parameters:
            mode: 
                zero: padding with 0
                norm: padding with normal distribution
            location: start / end
        """
        assert value in ['zero', 'norm'], "Padding value must be 'zero' or 'norm'"
        assert location in ['start', 'end'], "Padding location must be 'start' or 'end'"

        length = feature.shape[0]
        if length >= MAX_LEN:
            return feature[:MAX_LEN, :]
        
        if value == "zero":
            pad = np.zeros([MAX_LEN - length, feature.shape[-1]])
        elif value == "normal":
            mean, std = feature.mean(), feature.std()
            pad = np.random.normal(mean, std, (MAX_LEN-length, feature.shape[1]))

        feature = np.concatenate((pad, feature), axis=0) if(location == "start") else \
                  np.concatenate((feature, pad), axis=0)
        return feature

    def __paddingSequence(self, sequences, value, location):
        """
        Pad features to the same length according to the mean length of the features.
        """
        feature_dim = sequences[0].shape[-1]
        lengths = [s.shape[0] for s in sequences]
        # use (mean + 3 * std) as the max length
        final_length = int(np.mean(lengths) + 3 * np.std(lengths))
        final_sequence = np.zeros([len(sequences), final_length, feature_dim])
        for i, s in enumerate(sequences):
            if len(s) != 0:
                final_sequence[i] = self.__padding(s, final_length, value, location)
        return final_sequence, final_length

    def __collate_fn(self, batch):
        res = None
        for b in batch: # need to iterate through batch in case the first sample is bad(None)
            if b is not None:
                res = {k: [] for k in b.keys()} # initialize res
                break
        if res is None: # if all samples in this batch are bad(None), return None
            return None
        for b in batch:
            if b is None: # if one sample is bad(None), skip it
                continue
            for k, v in b.items():
                res[k].append(v)
        return res

    def __save_result(self, result, out_file):
        if osp.exists(out_file):
            out_file_alt = osp.splitext(out_file)[0] + '_' + str(int(time.time())) + '.pkl'
            self.logger.warning(f"Output file '{out_file}' already exists. Saving to '{out_file_alt}' instead.")
            out_file = out_file_alt
        Path(out_file).parent.mkdir(parents=True, exist_ok=True)
        with open(out_file, 'wb') as f:
            pickle.dump(result, f)
        self.logger.info(f"Feature file saved: '{out_file}'.")
    
    def __save_tmp_result(self, tmp_res, out_file):
        pass

    def __load_tmp_result(self, tmp_res_file):
        pass

    def __remove_tmp_folder(self, tmp_dir):
        if osp.exists(tmp_dir):
            shutil.rmtree(tmp_dir)

    def run_single(self, in_file, out_file=None, text_file=None, return_type='np'):
        """
        Extract features from single file.

        Parameters:
            in_file: path to input video file.
            return_type: 'pt' for pytorch tensor, 'np' for numpy array. Default: 'np'.
            out_file (optional): path to output file.
            text_file (optional): path to text file.
        
        Returns:
            final_result: dictionary of extracted features.
        """
        try:
            self.__init_extractors()
            self.logger.info(f"Extracting features from '{in_file}'.")
            final_result = {}
            if 'audio' in self.config:
                audio_result = self.__audio_extract_single(in_file, keep_tmp_file=True)
            if 'video' in self.config:
                video_result = self.__video_extract_single(in_file)
            if 'text' in self.config:
                if text_file is None:
                    raise ValueError("Text file is not specified.")
                text_result = self.__text_extract_single(text_file)
            # combine audio and video features
            if return_type == 'pt':
                if 'audio' in self.config:
                    final_result['audio'] = torch.from_numpy(audio_result)
                if 'video' in self.config:
                    final_result['video'] = torch.from_numpy(video_result)
                if 'text' in self.config:
                    final_result['text'] = torch.from_numpy(text_result)
            elif return_type == 'np':
                if 'audio' in self.config:
                    final_result['audio'] = audio_result
                if 'video' in self.config:
                    final_result['video'] = video_result
                if 'text' in self.config:
                    final_result['text'] = text_result
            else:
                raise ValueError(f"Invalid return type '{return_type}'.")
            # save result
            if out_file:
                self.__save_result(final_result, out_file)
            return final_result
        except Exception as e:
            self.logger.exception("An Error Occured:")
            self.logger.debug("Removing temporary files.")
            self.__remove_tmp_folder(self.tmp_dir)
            raise e

    def run_dataset(self, dataset_name=None, dataset_root_dir=None, dataset_dir=None, out_file=None, return_type='np', num_workers=4,
                    batch_size=32, skip_bad_data=True, padding_value='zero', padding_location='end', face_detection_failure='skip', progress_q=None, task_id=None):
        """
        Extract features from dataset and save in MMSA compatible format.

        Parameters:
            dataset_name: name of dataset. Either 'dataset_name' or 'dataset_dir' must be specified.
            dataset_root_dir: root directory of dataset. If specified, will override 'dataset_root_dir' set when initializing MSA-FET.
            dataset_dir: Path to dataset directory. If specified, will override 'dataset_name'. Either 'dataset_name' or 'dataset_dir' must be specified.
            out_file: output feature file. If not specified, features will be saved under the dataset directory with the name 'feature.pkl'.
            return_type: 'pt' for pytorch tensor, 'np' for numpy array. Default: 'np'.
            num_workers: number of workers for parallel processing. Default: 4.
            batch_size: batch size for parallel processing. Default: 32.
            skip_bad_data: skip bad data when loading dataset. Default: True.
            padding_value: padding value for sequence padding. 'zero' or 'norm'. Default: 'zero'.
            padding_location: padding location for sequence padding. 'end' or 'start'. Default: 'end'.
            face_detection_failure: action to take when face detection fails. 'skip' the frame or 'pad' with zeros. Default: 'skip'.
            progress_q: multiprocessing queue for progress reporting with M-SENA.
            task_id: task id for M-SENA.
        """
        # TODO: add database operation for M-SENA
        try:
            self.label_df, self.dataset_dir, self.dataset_name, self.dataset_config = \
                self.__read_label_file(dataset_name, dataset_root_dir, dataset_dir)
            
            self.logger.info(f"Extracting features from '{self.dataset_name}' dataset.")
            self.logger.info(f"Dataset directory: '{self.dataset_dir}'")

            self.report = None
            if type(progress_q) == multiprocessing.queues.Queue and task_id is not None:
                self.report = {'task_id': task_id, 'msg': 'Preparing', 'processed': 0, 'total': 0}
                progress_q.put(self.report)

            data = {
                "id": [], 
                "audio": [],
                "vision": [],
                "raw_text": [],
                "text": [],
                "text_bert": [],
                "audio_lengths": [],
                "vision_lengths": [],
                "annotations": [],
                # "classification_labels": [],  # no longer supported by MMSA
                "regression_labels": [],
                'regression_labels_A': [],
                'regression_labels_V': [],
                'regression_labels_T': [],
                "mode": []
            }

            dataloader = DataLoader(
                FET_Dataset(
                    self.label_df, self.dataset_dir, self.dataset_name,
                    self.config, self.dataset_config, self.tmp_dir, ignore_error=skip_bad_data
                ),
                batch_size=batch_size,
                num_workers=num_workers,
                shuffle=False,
                collate_fn=self.__collate_fn,
                # multiprocessing_context='spawn'
                # Using 'spawn' instead of 'fork' lead to more errors
                # Pytorch dataloader currently does not support cuda multiprocessing
                # Watch https://github.com/pytorch/pytorch/issues/41292 for updates
                # Currently only cpu is supported for dataset feature extraction
            )
            if self.report is not None:
                self.report['msg'] = 'Processing'
                self.report['total'] = len(dataloader)
                progress_q.put(self.report)
            for i, batch_data in enumerate(tqdm(dataloader)):
                if batch_data is None: # if all samples in this batch are bad(None), skip the batch
                    continue
                for k, v in batch_data.items():
                    data[k].extend(v)
                if self.report is not None:
                    self.report['processed'] = i + 1
                    progress_q.put(self.report)
            if self.report is not None:
                self.report['msg'] = 'Finalizing'
                progress_q.put(self.report)
            
            # remove unimodal labels if not exist
            for key in ['regression_labels_A', 'regression_labels_V', 'regression_labels_T']:
                if np.isnan(np.sum(data[key])):
                    data.pop(key)
            # remove empty features
            for key in ['audio', 'vision', 'text', 'text_bert', 'audio_lengths', 'vision_lengths']:
                if len(data[key]) == 0:
                    data.pop(key)
            # padding features
            for item in ['audio', 'vision', 'text', 'text_bert']:
                if item in data:
                    data[item], final_length = self.__paddingSequence(data[item], padding_value, padding_location)
                    if f"{item}_lengths" in data:
                        for i, length in enumerate(data[f"{item}_lengths"]):
                            if length > final_length:
                                data[f"{item}_lengths"][i] = final_length
            # transpose text_bert
            if 'text_bert' in data:
                data['text_bert'] = data['text_bert'].transpose(0, 2, 1)
            # repack features
            idx_dict = {
                mode + '_index': [i for i, v in enumerate(data['mode']) if v == mode]
                for mode in ['train', 'valid', 'test']
            }
            data.pop('mode')
            final_data = {k: {} for k in ['train', 'valid', 'test']}
            for mode in ['train', 'valid', 'test']:
                indexes = idx_dict[mode + '_index']
                for item in data.keys():
                    if isinstance(data[item], list):
                        final_data[mode][item] = np.array([data[item][v] for v in indexes])
                    else:
                        final_data[mode][item] = data[item][indexes]
            data = final_data
            # convert labels to numpy array

            # convert to pytorch tensors
            if return_type == 'pt':
                for mode in data.keys():
                    for key in ['audio', 'vision', 'text', 'text_bert']:
                        if key in data[mode]:
                            data[mode][key] = torch.from_numpy(data[mode][key])
            # save result
            if out_file is None:
                out_file = osp.join(self.dataset_dir, 'feature.pkl')
            self.__save_result(data, out_file)
            self.logger.info(f"Feature extraction complete!")
            if self.report is not None:
                self.report['msg'] = 'Finished'
                progress_q.put(self.report)
            return data
        except KeyboardInterrupt:
            self.logger.info("User aborted feature extraction!")
            self.__remove_tmp_folder(self.tmp_dir)
            if self.report is not None:
                self.report['msg'] = 'Terminated'
                progress_q.put(self.report)
        except Exception as e:
            self.logger.exception("An Error Occured:")
            self.logger.info("Removing temporary files.")
            self.__remove_tmp_folder(self.tmp_dir)
            if self.report is not None:
                self.report['msg'] = 'Error'
                progress_q.put(self.report)
            raise e

