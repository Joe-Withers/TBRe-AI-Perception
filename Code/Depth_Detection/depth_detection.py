import numpy as np

class Object_Depth_Detector():
    def __init__(self):
        print('initilise')

    def __str__(self):
        return 'class/object description'

    def calculate_depth(self, depth_slice):
        """Calculates the trimmed minimum (closest distance within 2 standard deviations of the mean) depth within a
        given slice."""
        depths = depth_slice.flatten()
        mean = np.mean(depths)
        standard_deviation = np.std(depths)
        upper_bound = mean + 2 * standard_deviation
        lower_bound = mean - 2 * standard_deviation
        trimmed_depths = np.where(np.logical_and(depths > lower_bound, depths < upper_bound))
        trimmed_minimum = np.min(trimmed_depths)
        return trimmed_minimum

    def get_depth(self, object_dicts, depth_maps):
        """ Input locations (bounding boxes) and depth map. Returns objects depths"""
        n = object_dicts["num_detections"]
        boxes = object_dicts["detection_boxes"]
        box_depths = np.empty(n)
        for i in range(n):
            box = boxes[i]
            top_left = np.array([box[0] * np.size(depth_maps, 1), box[1] * np.size(depth_maps, 0)])
            bottom_right = np.array([box[2] * np.size(depth_maps, 1), box[3] * np.size(depth_maps, 0)])
            depth_slice = depth_maps.slice(top_left, bottom_right)
            box_depths[i] = self.calculate_depth(depth_slice)
        return box_depths
