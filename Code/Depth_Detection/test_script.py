import unittest
import numpy as np
from depth_detection import Object_Depth_Detector

d = {
    'num_detections': 3,
    'detection_boxes': [[0.363644, 0.351542, 0.567458, 0.184534],
                        [0.456563, 0.537373, 0.757473, 0.2737467],
                        [0.4457457, 0.274467, 0.9453737, 0.145747]],
    'detection_scores': [0.45356, 0.34626, 0.135788],
    'detection_classes': [1, 1, 1]
}

depth_maps = [[5, 2, 5, 4], [8, 3, 2, 9], [4, 2, 7, 1]]

objectDepthDetector = Object_Depth_Detector()
objectDepthDetector.get_depth(d, depth_maps)
