

class Triangulation():
    def __init__(self):
        print('initilise')

    def __str__(self):
        return 'class/object description'

    def triangulate(self, images, object_dict, depth_maps):
        """ Input image that is a numpy array with shape [num_of_images, image_width,
        image_height, channels] ... returns the estimated 3D positions of the cones"""
        return None

class Matching():
    def __init__(self):
        print('initilise')

    def __str__(self):
        return 'class/object description'

    def match_objects(self, images, object_dict):
        """ Input image that is a numpy array with shape [num_of_images, image_width,
        image_height, channels] ... returns 2D correspondences"""
        return None
