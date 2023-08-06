# Copyright 2022 AI Singapore
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Detector class to handle detection of bboxes for efficientdet
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import tensorflow as tf


from peekingduck.pipeline.nodes.model.efficientdet_d04.efficientdet_files.model_process import (
    postprocess_boxes,
    preprocess_image,
)
from peekingduck.utils.graph_functions import load_graph


class Detector:
    """Detector class to handle detection of bboxes for efficientdet"""

    def __init__(
        self, config: Dict[str, Any], model_dir: Path, class_names: Dict[str, int]
    ) -> None:
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.model_dir = model_dir
        self.class_names = class_names
        self.effdet = self._create_effdet_model()

    def _create_effdet_model(self) -> tf.keras.Model:
        self.model_type = self.config["model_type"]
        graph_path = (
            self.model_dir / self.config["weights"]["model_file"][self.model_type]
        )

        model_nodes = self.config["MODEL_NODES"]
        model = load_graph(
            str(graph_path),
            inputs=model_nodes["inputs"],
            outputs=model_nodes["outputs"],
        )
        self.logger.info(
            "Efficientdet graph model loaded with following configs: \n\t"
            f"Model type: D{self.model_type}, \n\t"
            f"Score Threshold: {self.config['score_threshold']}, "
        )

        return model

    @staticmethod
    def preprocess(image: np.ndarray, image_size: int) -> Tuple[np.ndarray, float]:
        """Preprocessing function for efficientdet

        Args:
            image (np.ndarray): image in numpy array
            image_size (int): image size as defined in efficientdet config

        Returns:
            image (np.ndarray): the preprocessed image
            scale (float): the scale the image was resized to
        """
        image, scale = preprocess_image(image, image_size=image_size)
        return image, scale

    def postprocess(
        self,
        network_output: Tuple[np.ndarray, np.ndarray, np.ndarray],
        scale: float,
        img_shape: List[int],
        detect_ids: List[int],
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Postprocessing of detected bboxes for efficientdet

        Args:
            network_output (list): list of boxes, scores and labels from network
            scale (float): scale the image was resized to
            img_shape (list): height of original image
            detect_ids (list): list of label ids to be detected

        Returns:
            boxes (np.ndarray): postprocessed array of detected bboxes
            scores (np.ndarray): postprocessed array of scores
            labels (np.ndarray): postprocessed array of labels
        """
        img_h, img_w = img_shape
        boxes, scores, labels = network_output
        boxes = postprocess_boxes(boxes, scale, img_h, img_w)

        indices = np.where(scores[:] > self.config["score_threshold"])[0]

        # select those detections
        boxes = boxes[indices]
        labels = labels[indices]
        scores = scores[indices]

        detect_filter = np.where(np.isin(labels, detect_ids))
        boxes = boxes[detect_filter]
        labels = labels[detect_filter]
        scores = scores[detect_filter]

        if labels.size:
            labels = np.vectorize(self.class_names.get)(labels)
        return boxes, labels, scores

    def predict_object_bbox_from_image(
        self, image: np.ndarray, detect_ids: List[int]
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Efficientdet bbox prediction function

        Args:
            image (np.ndarray): image in numpy array
            detect_ids (list): list of label ids to be detected

        Returns:
            boxes (np.ndarray): array of detected bboxes
            labels (np.ndarray): array of labels
            scores (np.ndarray): array of scores
        """
        img_shape = image.shape[:2]

        image_size = self.config["size"][self.model_type]
        image, scale = self.preprocess(image, image_size=image_size)

        # run network
        graph_input = tf.convert_to_tensor(
            np.expand_dims(image, axis=0), dtype=tf.float32
        )
        boxes, scores, labels = self.effdet(x=graph_input)
        network_output = (
            np.squeeze(boxes.numpy()),
            np.squeeze(scores.numpy()),
            np.squeeze(labels.numpy()),
        )

        boxes, labels, scores = self.postprocess(
            network_output, scale, img_shape, detect_ids
        )

        return boxes, labels, scores
