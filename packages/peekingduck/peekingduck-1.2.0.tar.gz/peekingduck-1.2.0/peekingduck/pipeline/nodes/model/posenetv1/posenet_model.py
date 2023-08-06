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

"""PoseNet model with model types: mobilenet50, mobilenet75, mobilenet100 and resnet"""

import logging
from typing import Dict, Any, Tuple
import numpy as np

from peekingduck.weights_utils import checker, downloader, finder
from peekingduck.pipeline.nodes.model.posenetv1.posenet_files.predictor import Predictor


class PoseNetModel:  # pylint: disable=too-few-public-methods
    """PoseNet model with model types: mobilenet50, mobilenet75, mobilenet100 and resnet"""

    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__()

        self.logger = logging.getLogger(__name__)

        # check threshold values
        if not 0 <= config["score_threshold"] <= 1:
            raise ValueError("score_threshold must be in [0, 1]")
        if config["model_type"] not in [50, 75, 100, "resnet"]:
            raise ValueError("model_type must be one of [50, 75, 100, resnet]")

        weights_dir, model_dir = finder.find_paths(
            config["root"], config["weights"], config["weights_parent_dir"]
        )

        # check for posenet weights, if none then download into weights folder
        if not checker.has_weights(weights_dir, model_dir):
            self.logger.info("---no weights detected. proceeding to download...---")
            downloader.download_weights(weights_dir, config["weights"]["blob_file"])
            self.logger.info(f"---weights downloaded to {weights_dir}.---")

        self.predictor = Predictor(config, model_dir)

    def predict(
        self, frame: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """ Predict poses from input frame

        Args:
            frame (np.array): image in numpy array

        Returns:
            bboxes, keypoints, keypoint_scores, keypoint_masks, keypoint_conns
            (Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]): \
            tuple containing list of bboxes and pose related info i.e coordinates,
            scores, connections
        """
        assert isinstance(frame, np.ndarray)

        return self.predictor.predict(frame)
