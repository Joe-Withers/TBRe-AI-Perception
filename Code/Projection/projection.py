import numpy as np

fx = 0.002
fy = 0.002
intrinsic_matrix = [[fx,0,0],[0,fy,0],[0,0,1]]

def project(box, depth, image_size):
    if depth==None:
        return None
    else:
        [ymin, xmin, ymax, xmax] = box
        center_offset = [((ymin+ymax)/2)-0.5, ((xmin+xmax)/2)-0.5]
        center_offset_pixels = image_size*center_offset
        pixel_coordinates = [center_offset_pixels[0], center_offset_pixels[1], 1]#homogeneous 2D pixel coordinate relative to the center of the image
        camera_coordinates = np.matmul(intrinsic_matrix,pixel_coordinates)#use the camera intrinsic matrix (i.e. the focal length) to convert to camera coordinates
        relative_world_coordinates = (camera_coordinates*depth)/np.sum(camera_coordinates**2)#use some simple geometry to map out to world coordinates at correct depth
        # print(pixel_coordinates)
        # print(camera_coordinates)
        # print(relative_world_coordinates)
        return relative_world_coordinates


class Projection():
    def __init__(self):
        print('initilise')

    def __str__(self):
        return 'class/object description'

    def project_to_3d(self, boxes, depths, image_size):
        image_size = np.array(image_size)[0:1]
        """ Input: object 2d location (on image plane), depths of objects, and relevant info about the camera i.e. focal length.
        returns the estimated 3D positions of the cones"""
        points3d = [project(box,depth,image_size) for box, depth in zip(boxes, depths)]
        return points3d
