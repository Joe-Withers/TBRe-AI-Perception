import numpy as np

class Object_Matcher():
    def __init__(self):
        print('initialise')

    def __str__(self):
        return 'class/object description'

    def match_objects(self, images, object_dict):
        """ Input image that is a numpy array with shape [num_of_images, image_width,
        image_height, channels] ... returns 2D correspondences"""
        for image in images:
            slices = list()
            # Let fullImage = <the image>
            for boundingBox in boundingBoxes:
                # Let topLeft = <the coordinate of the top left of the bounding box>
                # Let bottomRight = <the coordinate of the bottom right of the bounding box>
                imageSlice = fullImage[slice(topLeft, bottomRight)]
                slices.append(imageSlice)

        return None
