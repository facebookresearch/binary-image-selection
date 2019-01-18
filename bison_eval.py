#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import os
import json
import argparse

import numpy as np


class BisonEval:
    def __init__(self, anno, pred):
        if pred.getBisonIds() != anno.getBisonIds():
            print('[Warning] The prediction does not' +
                  'cover the entire set of bison data.' +
                  'The evaluation is running on the {}'.format(
                        len(pred.getBisonIds())) +
                  'subset from prediction file.')
        self.params = {'bison_ids': pred.getBisonIds()}
        self.anno = anno
        self.pred = pred

    def evaluate(self):
        accuracy = []
        for bison_id in self.params['bison_ids']:
            accuracy.append(self.anno[bison_id]['true_image_id'] ==
                            self.pred[bison_id])
        mean_accuracy = np.mean(accuracy)
        print("[Result] Mean BISON accuracy on {}: {:.2f}%".format(
            self.anno.dataset, mean_accuracy * 100)
        )
        return mean_accuracy


class Annotation:
    def __init__(self, anno_filepath):
        assert os.path.exists(anno_filepath), 'Annotation file does not exist'
        with open(anno_filepath) as fd:
            anno_results = json.load(fd)
        self._data = {res['bison_id']: res for res in anno_results['data']}
        self.dataset = "{}.{}".format(anno_results['info']['source'],
                                      anno_results['info']['split'])

    def getBisonIds(self):
        return self._data.keys()

    def __getitem__(self, key):
        return self._data[key]


class Prediction:
    def __init__(self, pred_filepath):
        assert os.path.exists(pred_filepath), 'Prediction file does not exist'
        with open(pred_filepath) as fd:
            pred_results = json.load(fd)

        self._data = {result['bison_id']: result['predicted_image_id']
                      for result in pred_results}

    def getBisonIds(self):
        return self._data.keys()

    def __getitem__(self, key):
        return self._data[key]


def _command_line_parser():
    parser = argparse.ArgumentParser()
    default_anno = './annotations/bison_annotations.cocoval2014.json'
    default_pred = './predictions/fake_predictions.cocoval2014.json'
    parser.add_argument('--anno_path', default=default_anno,
                        help='Path to the annotation file')
    parser.add_argument('--pred_path', default=default_pred,
                        help='Path to the prediction file')
    return parser


def main(args):
    anno = Annotation(args.anno_path)
    pred = Prediction(args.pred_path)
    bison = BisonEval(anno, pred)
    bison.evaluate()


if __name__ == '__main__':
    parser = _command_line_parser()
    args = parser.parse_args()
    main(args)
