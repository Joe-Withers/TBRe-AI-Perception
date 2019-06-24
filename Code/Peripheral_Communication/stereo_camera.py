import time
import pyzed.sl as sl
import math, sys
import scipy.io as sio
import cv2
import numpy as np

def regularize_image(im):
    im += np.min(im)
    return im/np.max(im)


class Stereo_Camera():
    def __init__(self):
        # Create a Camera object
        self.zed = sl.Camera()

        # Create a InitParameters object and set configuration parameters
        init_params = sl.InitParameters()
        init_params.camera_resolution = sl.RESOLUTION.RESOLUTION_HD720  # Use HD720 video mode (default fps: 60)
        # Use a right-handed Y-up coordinate system
        init_params.coordinate_system = sl.COORDINATE_SYSTEM.COORDINATE_SYSTEM_RIGHT_HANDED_Y_UP
        # init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_PERFORMANCE  # Use PERFORMANCE depth mode
        init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_ULTRA  # Use PERFORMANCE depth mode
        init_params.coordinate_units = sl.UNIT.UNIT_MILLIMETER  # Use milliliter units (for depth measurements)
        # init_params.coordinate_units = sl.UNIT.UNIT_METER  # Set units in meters

        # Open the camera
        err = self.zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            exit(1)

    def get_new_frames(self):
        # Create and set RuntimeParameters after opening the camera
        runtime_parameters = sl.RuntimeParameters()
        runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_STANDARD  # Use STANDARD sensing mode
        # Capture 50 images and depth, then stop
        i = 0
        image = sl.Mat()
        # depth_im = sl.Mat()
        depth = sl.Mat()
        point_cloud = sl.Mat()
        imc = []
        d = []
        while i < 1:
            # A new image is available if grab() returns SUCCESS
            if self.zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                self.zed.retrieve_image(image, sl.VIEW.VIEW_LEFT)
                # Retrieve depth map. Depth is aligned on the left image
                # self.zed.retrieve_image(depth_im, sl.VIEW.VIEW_DEPTH)
                self.zed.retrieve_measure(depth, sl.MEASURE.MEASURE_DEPTH)
                i += 1

                # if 0:
                #     # Retrieve colored point cloud. Point cloud is aligned on the left image.
                #     self.zed.retrieve_measure(point_cloud, sl.MEASURE.MEASURE_XYZRGBA)
                #     # Get and print distance value in mm at the center of the image
                #     # We measure the distance camera - object using Euclidean distance
                #     x = round(image.get_width() / 2)
                #     y = round(image.get_height() / 2)
                #     err, point_cloud_value = point_cloud.get_value(x, y)
                #
                #     distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                #                          point_cloud_value[1] * point_cloud_value[1] +
                #                          point_cloud_value[2] * point_cloud_value[2])
                #
                #     if not np.isnan(distance) and not np.isinf(distance):
                #         distance = round(distance)
                #         print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                #         # Increment the loop
                #         i = i + 1
                #     else:
                #         print("Can't estimate distance at this position, move the camera\n")

                sys.stdout.flush()

        imc = image.get_data()[:,:,:3]
        depth_data = depth.get_data()
        depth_data[np.isnan(depth_data)] = 0
        depth_data[np.isinf(depth_data)] = 0
        depth_data[depth_data<0] = 0
        # print(depth_data.shape)
        # cv2.imshow('depth '+str(i), regularize_image(depth_data))
        # cv2.waitKey(0)
        images = np.expand_dims(np.array(imc), axis=0)
        depth_maps = np.expand_dims(np.array(depth_data), axis=0)
        return images, depth_maps

    def __str__(self):
        return 'class/object description'

    def close_cam(self):
        # Close the camera
        self.zed.close()

    #temporary function for testing without camera
    def generate_image_and_depth(self, depth_filename = './Peripheral_Communication/example_inputs/150_depth.mat',
    im_filename = './Peripheral_Communication/example_inputs/150_im.png'):
        m = sio.loadmat(depth_filename)
        depth = m['d']
        print(depth)
        image = cv2.imread(im_filename)
        return image, depth

class Stereo_Camera_test():
    def __init__(self):
        # Create a Camera object
        self.zed = sl.Camera()

        # Create a InitParameters object and set configuration parameters
        init_params = sl.InitParameters()
        init_params.camera_resolution = sl.RESOLUTION.RESOLUTION_HD720  # Use HD720 video mode (default fps: 60)
        # Use a right-handed Y-up coordinate system
        init_params.coordinate_system = sl.COORDINATE_SYSTEM.COORDINATE_SYSTEM_RIGHT_HANDED_Y_UP
        # init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_PERFORMANCE  # Use PERFORMANCE depth mode
        init_params.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_ULTRA  # Use PERFORMANCE depth mode
        init_params.coordinate_units = sl.UNIT.UNIT_MILLIMETER  # Use milliliter units (for depth measurements)
        # init_params.coordinate_units = sl.UNIT.UNIT_METER  # Set units in meters

        # Open the camera
        err = self.zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            exit(1)

    def get_image_and_depth(self):
        # Create and set RuntimeParameters after opening the camera
        runtime_parameters = sl.RuntimeParameters()
        runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_STANDARD  # Use STANDARD sensing mode
        # Capture 50 images and depth, then stop
        i = 0
        image = sl.Mat()
        # depth_im = sl.Mat()
        depth = sl.Mat()
        point_cloud = sl.Mat()
        imc = []
        d = []
        while i < 1:
            # A new image is available if grab() returns SUCCESS
            if self.zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                self.zed.retrieve_image(image, sl.VIEW.VIEW_LEFT)
                # Retrieve depth map. Depth is aligned on the left image
                # self.zed.retrieve_image(depth_im, sl.VIEW.VIEW_DEPTH)
                self.zed.retrieve_measure(depth, sl.MEASURE.MEASURE_DEPTH)
                i += 1
                sys.stdout.flush()

        imc = image.get_data()[:,:,:3]
        depth_data = depth.get_data()
        depth_data[np.isnan(depth_data)] = 0
        depth_data[np.isinf(depth_data)] = 0
        depth_data[depth_data<0] = 0
        print(depth_data.shape)
        cv2.imshow('depth '+str(i), regularize_image(depth_data))
        cv2.waitKey(0)
        return imc, depth_data

    def close_cam(self):
        # Close the camera
        self.zed.close()


if __name__ == "__main__":
    s = Stereo_Camera_test()
    for i in range(10):
        s.get_image_and_depth()
    s.close_cam()
