# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Finetuning the library models for sequence classification on clinical NLP tasks"""


import dataclasses
import logging
import os
from os.path import basename, dirname
import sys
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, List, Union
from filelock import FileLock
import time
import tempfile
import math

from enum import Enum

import numpy as np
from seqeval.metrics.sequence_labeling import get_entities

import torch
from torch.utils.data.dataset import Dataset
from transformers import AutoConfig, AutoTokenizer, AutoModel, EvalPrediction
from transformers.training_args import IntervalStrategy
from transformers.data.processors.utils import InputFeatures
from transformers.tokenization_utils import PreTrainedTokenizer
from transformers.data.metrics import acc_and_f1
from transformers.data.processors.utils import DataProcessor, InputExample, InputFeatures
from transformers import ALL_PRETRAINED_CONFIG_ARCHIVE_MAP
from transformers.optimization import AdamW, get_scheduler
from transformers.trainer_pt_utils import get_parameter_names
from transformers.file_utils import hf_bucket_url, CONFIG_NAME

from .cnlp_processors import cnlp_processors, cnlp_output_modes, cnlp_compute_metrics, tagging, relex, classification
from .cnlp_data import ClinicalNlpDataset, DataTrainingArguments

from .CnlpModelForClassification import CnlpModelForClassification, CnlpConfig
from .BaselineModels import CnnSentenceClassifier, LstmSentenceClassifier
from .HierarchicalTransformer import HierarchicalModel, HierarchicalTransformerConfig

import requests

from transformers import (
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    set_seed,
)

cnlpt_models = ['cnn', 'lstm', 'hier', 'cnlpt']

logger = logging.getLogger(__name__)

@dataclass
class CnlpTrainingArguments(TrainingArguments):
    """
    Additional arguments specific to this class
    """
    evals_per_epoch: Optional[int] = field(
        default = -1, metadata={"help": "Number of times to evaluate and possibly save model per training epoch (allows for a lazy kind of early stopping)"}
    )
    final_task_weight: Optional[float] = field(
        default=1.0, metadata={"help": "Amount to up/down-weight final task in task list (other tasks weighted 1.0)"}
    )
    freeze: bool = field(
        default=False, metadata={"help": "Freeze the encoder layers and only train the layer between the encoder and classification architecture. Probably works best with --token flag since [CLS] may not be well-trained for anything in particular."}
    )
    arg_reg: Optional[float] = field(
        default=-1, metadata={"help": "Weight to use on argument regularization term (penalizes end-to-end system if a discovered relation has low probability of being any entity type). Value < 0 (default) turns off this penalty."}
    )
    bias_fit: bool = field(
        default=False, metadata={"help": "Only optimize the bias parameters of the encoder (and the weights of the classifier heads), as proposed in the BitFit paper by Ben Zaken et al. 2021 (https://arxiv.org/abs/2106.10199)"}
    )

@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """
    model: Optional[str] = field( default='cnlpt', 
        metadata={'help': "Model type", 'choices':cnlpt_models}
    )
    encoder_name: Optional[str] = field(default='roberta-base',
        metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models"}
    )
    config_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained config name or path if not the same as model_name"}
    )
    tokenizer_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained tokenizer name or path if not the same as model_name"}
    )
    cache_dir: Optional[str] = field(
        default=None, metadata={"help": "Where do you want to store the pretrained models downloaded from s3"}
    )
    layer: Optional[int] = field(
        default=-1, metadata={"help": "Which layer's CLS ('<s>') token to use"}
    )
    token: bool = field(
        default=False, metadata={"help": "Classify over an actual token rather than the [CLS] ('<s>') token -- requires that the tokens to be classified are surrounded by <e>/</e> tokens"}
    )
    num_rel_feats: Optional[int] = field(
        default=12, metadata={"help": "Number of features/attention heads to use in the NxN relation classifier"}
    )
    head_features: Optional[int] = field(
        default=64, metadata={"help": "Number of parameters in each attention head in the NxN relation classifier"}
    )
    use_prior_tasks: bool = field(
        default=False, metadata={"help": "In the multi-task setting, incorporate the logits from the previous tasks into subsequent representation layers. This will be done in the task order specified in the command line."}
    )
    hier_num_layers: Optional[int] = field(
        default=2,
        metadata={
            "help": (
                "For the hierarchical model, the number of document-level transformer "
                "layers"
            )
        },
    )
    hier_hidden_dim: Optional[int] = field(
        default=2048,
        metadata={
            "help": (
                "For the hierarchical model, the inner hidden size of the positionwise "
                "FFN in the document-level transformer layers"
            )
        },
    )
    hier_n_head: Optional[int] = field(
        default=8,
        metadata={
            "help": (
                "For the hierarchical model, the number of attention heads in the "
                "document-level transformer layers"
            )
        },
    )
    hier_d_k: Optional[int] = field(
        default=8,
        metadata={
            "help": (
                "For the hierarchical model, the size of the query and key vectors in "
                "the document-level transformer layers"
            )
        },
    )
    hier_d_v: Optional[int] = field(
        default=96,
        metadata={
            "help": (
                "For the hierarchical model, the size of the value vectors in the "
                "document-level transformer layers"
            )
        },
    )


def is_pretrained_model(model_name):
    # check if it's a built-in pre-trained config:
    if model_name in ALL_PRETRAINED_CONFIG_ARCHIVE_MAP:
        return True
    
    # check if it's a model on the huggingface model hub:
    url = hf_bucket_url(model_name, CONFIG_NAME)
    r = requests.head(url)
    if r.status_code == 200:
        return True

    return False

def main():
    # See all possible arguments in src/transformers/training_args.py
    # or by passing the --help flag to this script.
    # We now keep distinct sets of args, for a cleaner separation of concerns.
    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, CnlpTrainingArguments))

    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        # If we pass only one argument to the script and it's the path to a json file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))
    else:
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    if (
        os.path.exists(training_args.output_dir)
        and os.listdir(training_args.output_dir)
        and training_args.do_train
        and not training_args.overwrite_output_dir
    ):
        raise ValueError(
            f"Output directory ({training_args.output_dir}) already exists and is not empty. Use --overwrite_output_dir to overcome."
        )

    assert len(data_args.task_name) == len(data_args.data_dir), 'Number of tasks and data directories should be the same!'

    
    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO if training_args.local_rank in [-1, 0] else logging.WARN,
    )
    logger.warning(
        "Process rank: %s, device: %s, n_gpu: %s, distributed training: %s, 16-bits training: %s" %
        (training_args.local_rank,
        training_args.device,
        training_args.n_gpu,
        bool(training_args.local_rank != -1),
        training_args.fp16)
    )
    logger.info("Training/evaluation parameters %s" % training_args)
    logger.info("Data parameters %s" % data_args)
    logger.info("Model parameters %s" % model_args)
    # Set seed
    set_seed(training_args.seed)

    try:
        task_names = []
        num_labels = []
        output_mode = []
        tagger = []
        relations = []
        for task_name in data_args.task_name:
            processor = cnlp_processors[task_name]()
            if processor.get_num_tasks() > 1:
                for subtask_num in range(processor.get_num_tasks()):
                    task_names.append(task_name + "-" + processor.get_classifiers()[subtask_num])
                    num_labels.append(len(processor.get_labels()))
                    output_mode.append(classification)
                    tagger.append(False)
                    relations.append(False)
            else:
                task_names.append(task_name)
                num_labels.append(len(processor.get_labels()))

                output_mode.append(cnlp_output_modes[task_name])
                tagger.append(cnlp_output_modes[task_name] == tagging)
                relations.append(cnlp_output_modes[task_name] == relex)

    except KeyError:
        raise ValueError("Task not found: %s" % (data_args.task_name))

    # Load tokenizer: Need this first for loading the datasets
    tokenizer = AutoTokenizer.from_pretrained(
        model_args.tokenizer_name if model_args.tokenizer_name else model_args.encoder_name,
        cache_dir=model_args.cache_dir,
        add_prefix_space=True,
        additional_special_tokens=['<e>', '</e>', '<a1>', '</a1>', '<a2>', '</a2>', '<cr>', '<neg>']
    )

    model_name = model_args.model
    hierarchical = model_name == 'hier'

    # Get datasets
    train_dataset = (
        ClinicalNlpDataset(data_args, tokenizer=tokenizer, cache_dir=model_args.cache_dir, hierarchical=hierarchical) if training_args.do_train else None
    )
    eval_dataset = (
        ClinicalNlpDataset(data_args, tokenizer=tokenizer, mode="dev", cache_dir=model_args.cache_dir, hierarchical=hierarchical)
        if training_args.do_eval
        else None
    )
    test_dataset = (
        ClinicalNlpDataset(data_args, tokenizer=tokenizer, mode="test", cache_dir=model_args.cache_dir, hierarchical=hierarchical)
        if training_args.do_predict
        else None
    )

    # Load pretrained model and tokenizer
    #
    # Distributed training:
    # The .from_pretrained methods guarantee that only one local process can concurrently
    # download model & vocab.

    pretrained = False

    if model_name == 'cnn':
        model = CnnSentenceClassifier(len(tokenizer), num_labels_list=num_labels)
    elif model_name == 'lstm':
        model = LstmSentenceClassifier(len(tokenizer), num_labels_list=num_labels)
    elif model_name == 'hier':
        # encoder_config = AutoConfig.from_pretrained(
        #     model_args.config_name if model_args.config_name else model_args.encoder_name,
        #     finetuning_task=data_args.task_name,
        # )

        pretrained = True

        encoder_name = model_args.config_name if model_args.config_name else model_args.encoder_name
        config = CnlpConfig(
            encoder_name,
            data_args.task_name,
            num_labels,
            layer=model_args.layer,
            tokens=model_args.token,
            num_rel_attention_heads=model_args.num_rel_feats,
            rel_attention_head_dims=model_args.head_features,
            tagger=tagger,
            relations=relations,
        )
        # num_tokens=len(tokenizer))
        config.vocab_size = len(tokenizer)

        encoder_dim = config.hidden_size

        transformer_head_config = HierarchicalTransformerConfig(
            n_layers=model_args.hier_num_layers,
            d_model=encoder_dim,
            d_inner=model_args.hier_hidden_dim,
            n_head=model_args.hier_n_head,
            d_k=model_args.hier_d_k,
            d_v=model_args.hier_d_v,
        )

        model = HierarchicalModel(
            config=config,
            transformer_head_config=transformer_head_config,
            class_weights=None if train_dataset is None else train_dataset.class_weights,
            final_task_weight=training_args.final_task_weight,
            freeze=training_args.freeze,
            argument_regularization=training_args.arg_reg,
        )

    else:
        # by default cnlpt model, but need to check which encoder they want
        encoder_name = model_args.encoder_name

        # TODO check when download any pretrained language model to local disk, if 
        # the following condition "is_pretrained_model(encoder_name)" works or not.
        if not is_pretrained_model(encoder_name):
            # we are loading one of our own trained models as a starting point.
            #
            # 1) if training_args.do_train is true:
            # sometimes we may want to use an encoder that has been had continued pre-training, either on
            # in-domain MLM or another task we think might be useful. In that case our encoder will just
            # be a link to a directory. If the encoder-name is not recognized as a pre-trianed model, special
            # logic for ad hoc encoders follows:
            # we will load it as-is initially, then delete its classifier head, save the encoder
            # as a temp file, and make that temp file
            # the model file to be loaded down below the normal way. since that temp file
            # doesn't have a stored classifier it will use the randomly-inited classifier head
            # with the size of the supplied config (for the new task).
            # TODO This setting 1) is not tested yet.
            # 2) if training_args.do_train is false:
            # we evaluate or make predictions of our trained models. 
            # Both two setting require the registeration of CnlpConfig, and use 
            # AutoConfig.from_pretrained() to load the configuration file
            AutoConfig.register("cnlpt", CnlpConfig)
            AutoModel.register(CnlpConfig, CnlpModelForClassification)

            
            # Load the cnlp configuration using AutoConfig, this will not override 
            # the arguments from trained cnlp models. While using CnlpConfig will override
            # the model_type and model_name of the encoder.
            config = AutoConfig.from_pretrained(
                model_args.config_name if model_args.config_name else model_args.encoder_name,
                cache_dir=model_args.cache_dir,
            )

            if training_args.do_train:
                # Setting 1) only load weights from the encoder
                raise NotImplementedError('This functionality has not been restored yet')
                model = CnlpModelForClassification(
                        model_path = model_args.encoder_name,
                        config=config,
                        cache_dir=model_args.cache_dir,
                        tagger=tagger,
                        relations=relations,
                        class_weights=None if train_dataset is None else train_dataset.class_weights,
                        final_task_weight=training_args.final_task_weight,
                        use_prior_tasks=model_args.use_prior_tasks,
                        argument_regularization=model_args.arg_reg)
                delattr(model, 'classifiers')
                delattr(model, 'feature_extractors')
                if training_args.do_train:
                    tempmodel = tempfile.NamedTemporaryFile(dir=model_args.cache_dir)
                    torch.save(model.state_dict(), tempmodel)
                    model_name = tempmodel.name
            else:
                # setting 2) evaluate or make predictions
                model = CnlpModelForClassification.from_pretrained(
                    model_args.encoder_name,
                    config=config,
                    class_weights=None if train_dataset is None else train_dataset.class_weights,
                    final_task_weight=training_args.final_task_weight,
                    freeze=training_args.freeze,
                    bias_fit=training_args.bias_fit,
                    argument_regularization=training_args.arg_reg)

        else:
            # This only works when model_args.encoder_name is one of the 
            # model card from https://huggingface.co/models
            # By default, we use model card as the starting point to fine-tune
            encoder_name = model_args.config_name if model_args.config_name else model_args.encoder_name
            config = CnlpConfig(encoder_name,
                                data_args.task_name,
                                num_labels,
                                layer=model_args.layer,
                                tokens=model_args.token,
                                num_rel_attention_heads=model_args.num_rel_feats,
                                rel_attention_head_dims=model_args.head_features,
                                tagger=tagger,
                                relations=relations,)
                                #num_tokens=len(tokenizer))
            config.vocab_size = len(tokenizer)
            pretrained = True
            model = CnlpModelForClassification(
                config=config,
                class_weights=None if train_dataset is None else train_dataset.class_weights,
                final_task_weight=training_args.final_task_weight,
                freeze=training_args.freeze,
                bias_fit=training_args.bias_fit,
                argument_regularization=training_args.arg_reg)

    best_eval_results = None
    output_eval_file = os.path.join(
        training_args.output_dir, f"eval_results.txt"
    )
    output_eval_predictions = os.path.join(
        training_args.output_dir, f'eval_predictions.txt'
    )

    if training_args.do_train:
        batches_per_epoch = math.ceil(len(train_dataset) / training_args.train_batch_size)
        total_steps = int(training_args.num_train_epochs * batches_per_epoch // training_args.gradient_accumulation_steps)

        if training_args.evals_per_epoch > 0:
            logger.warning('Overwriting the value of logging steps based on provided evals_per_epoch argument')
            # steps per epoch factors in gradient accumulation steps (as compared to batches_per_epoch above which doesn't)
            steps_per_epoch = int(total_steps // training_args.num_train_epochs)
            training_args.eval_steps = steps_per_epoch // training_args.evals_per_epoch
            training_args.evaluation_strategy = IntervalStrategy.STEPS
            # This will save model per epoch
            # training_args.save_strategy = IntervalStrategy.EPOCH
        elif training_args.do_eval:
            logger.info('Evaluation strategy not specified so evaluating every epoch')
            training_args.evaluation_strategy = IntervalStrategy.EPOCH

    def build_compute_metrics_fn(task_names: List[str], model) -> Callable[[EvalPrediction], Dict]:
        def compute_metrics_fn(p: EvalPrediction):

            metrics = {}
            task_scores = []
            task_label_ind = 0

            # if not p is list:
            #     p = [p]

            for task_ind,task_name in enumerate(task_names):
                if tagger[task_ind]:
                    preds = np.argmax(p.predictions[task_ind], axis=2)
                    # labels will be -100 where we don't need to tag
                elif relations[task_ind]:
                    preds = np.argmax(p.predictions[task_ind], axis=3)
                else:
                    preds = np.argmax(p.predictions[task_ind], axis=1)

                if len(task_names) == 1:
                    labels = p.label_ids[:,0]
                elif relations[task_ind]:
                    labels = p.label_ids[:,0,task_label_ind:task_label_ind+data_args.max_seq_length,:].squeeze()
                    task_label_ind += data_args.max_seq_length
                elif p.label_ids.ndim == 4:
                    labels = p.label_ids[:,0,task_label_ind:task_label_ind+1,:].squeeze()
                    task_label_ind += 1
                elif p.label_ids.ndim == 3:
                    labels = p.label_ids[:,0,task_label_ind:task_label_ind+1].squeeze()
                    task_label_ind += 1

                metrics[task_name] = cnlp_compute_metrics(task_name, preds, labels)
                processor = cnlp_processors.get(task_name, cnlp_processors.get(task_name.split('-')[0], None))()
                task_scores.append(processor.get_one_score(metrics.get(task_name, metrics.get(task_name.split('-')[0], None))))

            one_score = sum(task_scores) / len(task_scores)

            if not model is None:
                if not hasattr(model, 'best_score') or one_score > model.best_score:
                    if pretrained:
                        trainer.save_model()
                    # For convenience, we also re-save the tokenizer to the same directory,
                    # so that you can share your model easily on huggingface.co/models =)
                    if trainer.is_world_process_zero():
                        tokenizer.save_pretrained(training_args.output_dir)
                        for task_ind,task_name in enumerate(metrics):
                            with open(output_eval_file, "w") as writer:
                                logger.info("***** Eval results for task %s *****" % (task_name))
                                for key, value in metrics[task_name].items():
                                    logger.info("  %s = %s", key, value)
                                    writer.write("%s = %s\n" % (key, value))
                    model.best_score = one_score
                    model.best_eval_results = metrics

            return metrics

        return compute_metrics_fn

    # Initialize our Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        compute_metrics=build_compute_metrics_fn(task_names, model),
    )

    # Training
    if training_args.do_train:
        trainer.train(
            # resume_from_checkpoint=model_args.model_name_or_path if os.path.isdir(model_args.model_name_or_path) else None
        )

        if not hasattr(model, 'best_score'):
            if pretrained:
                trainer.save_model()
                # For convenience, we also re-save the tokenizer to the same directory,
                # so that you can share your model easily on huggingface.co/models =)
                if trainer.is_world_process_zero():
                    tokenizer.save_pretrained(training_args.output_dir)

    # Evaluation
    eval_results = {}
    if training_args.do_eval:
        logger.info("*** Evaluate ***")

        try:
            eval_result = model.best_eval_results
        except:
            eval_result = trainer.evaluate(eval_dataset=eval_dataset)
        
        if trainer.is_world_process_zero():
            with open(output_eval_file, "w") as writer:
                logger.info("***** Eval results *****")
                for key, value in eval_result.items():
                    logger.info("  %s = %s", key, value)
                    writer.write("%s = %s\n" % (key, value))

            with open(output_eval_predictions, 'w') as writer:
                #Chen wrote the below but it doesn't work for all settings
                predictions = trainer.predict(test_dataset=eval_dataset).predictions
                dataset_labels = eval_dataset.get_labels()
                for task_ind, task_name in enumerate(task_names):
                    if output_mode[task_ind] == classification:
                        task_predictions = np.argmax(predictions[task_ind], axis=1)
                        for index, item in enumerate(task_predictions):
                            if len(task_names) > len(dataset_labels):
                                subtask_ind = 0
                            else:
                                subtask_ind = task_ind
                            item = dataset_labels[subtask_ind][item]
                            writer.write("Task %d (%s) - Index %d - %s\n" % (task_ind, task_name, index, item))
                    elif output_mode[task_ind] == tagging:
                        task_predictions = np.argmax(predictions[task_ind], axis=2)
                        task_labels = dataset_labels[task_ind]
                        for index, pred_seq in enumerate(task_predictions):
                            wpind_to_ind = {}
                            chunk_labels = []

                            tokens = tokenizer.convert_ids_to_tokens(eval_dataset.features[index].input_ids)
                            for token_ind in range(1,len(tokens)):
                                if eval_dataset[index].input_ids[token_ind] <= 2:
                                    break
                                if tokens[token_ind].startswith('Ġ'):
                                    wpind_to_ind[token_ind] = len(wpind_to_ind)
                                    chunk_labels.append(task_labels[task_predictions[index][token_ind]])

                            entities = get_entities(chunk_labels)
                            writer.write('Task %d (%s) - Index %d: %s\n' % (task_ind, task_name, index, str(entities)))
                    elif output_mode[task_ind] == relex:
                        task_predictions = np.argmax(predictions[task_ind], axis=3)
                        task_labels = dataset_labels[task_ind]
                        assert task_labels[0] == 'None', 'The first labeled relation category should always be "None" but for task %s it is %s' % (task_names[task_ind], task_labels[0])
                        
                        for inst_ind in range(task_predictions.shape[0]):
                            inst_preds = task_predictions[inst_ind]
                            a1s, a2s = np.where(inst_preds > 0)
                            for arg_ind in range(len(a1s)):
                                a1_ind = a1s[arg_ind]
                                a2_ind = a2s[arg_ind]
                                cat = task_labels[ inst_preds[a1_ind][a2_ind] ]
                                writer.write("Task %d (%s) - Index %d - %s(%d, %d)\n" % (task_ind, task_name, inst_ind, cat, a1_ind, a2_ind))
                    else:
                        raise NotImplementedError('Writing predictions is not implemented for this output_mode!')

        eval_results.update(eval_result)

    if training_args.do_predict:
        logging.info("*** Test ***")
        # FIXME: this part hasn't been updated for the MTL setup so it doesn't work anymore since
        # predictions is generalized to be a list of predictions and the output needs to be different for each kin.
        # maybe it's ok to only handle classification since it has a very straightforward output format and evaluation,
        # while for relations we can punt to the user to just write their own eval code.
        predictions = trainer.predict(test_dataset=test_dataset).predictions
        for task_ind, task_name in enumerate(task_names):
            if output_mode[task_ind] == "classification":
                task_predictions = np.argmax(predictions[task_ind], axis=1)
            else:
                raise NotImplementedError('Writing predictions is not implemented for this output_mode!')
        
            output_test_file = os.path.join(
                training_args.output_dir, f"test_results.txt"
            )
            if trainer.is_world_process_zero():
                with open(output_test_file, "w") as writer:
                    logger.info("***** Test results *****")
                    for index, item in enumerate(task_predictions):
                        item = test_dataset.get_labels()[task_ind][item]
                        writer.write("%s\n" % (item))

    return eval_results


def _mp_fn(index):
    # For xla_spawn (TPUs)
    main()


if __name__ == "__main__":
    main()
