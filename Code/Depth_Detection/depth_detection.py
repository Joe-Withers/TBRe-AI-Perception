import numpy as np

class Object_Depth_Detector():
    def __init__(self):
        print('initilise')

    def __str__(self):
        return 'class/object description'

    def calculate_depth(self, depth_slice):
        """Calculates the trimmed mean depth within a given slice (excluding outliers that are at a distance of more
        than two standard deviations from the mean"""
        depths = depth_slice.flatten()
        mean = np.mean(depths)
        standard_deviation = np.std(depths)
        upper_bound = mean + 2 * standard_deviation
        lower_bound = mean - 2 * standard_deviation
        trimmed_depths = np.empty(np.size(depths))
        for i in range(np.size(depths)):
            if (depths[i] < upper_bound) and (depths[i] > lower_bound):
                trimmed_depths[i] = depths[i]
        trimmed_mean = np.mean(trimmed_depths)
        return trimmed_mean

    def get_depth(self, object_dicts, depth_maps):
        """ Input locations (bounding boxes) and depth map. Returns objects depths"""
        n = object_dicts["num_detections"]
        boxes = object_dicts["detection_boxes"]
        box_depths = np.empty(n)
        for i in range(n):
            box = boxes[i]
            top_left = np.array([box[0], box[1]])
            bottom_right = np.array([box[2], box[3]])
            depth_slice = depth_maps.slice(top_left, bottom_right)
            box_depths[i] = self.calculate_depth(depth_slice)
        boxes.append(box_depths, axis=1)
        # This array has n columns and two rows. The first row contains the bounding boxes [x,y,x,y] and the second row
        # contains the calculated depths of the objects bounded by those boxes.
        return None
