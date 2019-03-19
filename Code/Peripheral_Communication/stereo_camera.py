import time
from threading import Thread, Lock
import pyzed.sl as sl

class Stereo_Camera(Thread):
    def __init__(self, threadID, cam_name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = cam_name

        #using a lock to stop the flag from being updated at same time
        self.flag_lock = Lock()

        self.flag_lock.acquire()
        self._exit_flag = False
        self.flag_lock.release()

    def run(self):
        """ reads input frames from stereo camera (on a loop)
        Note: Always acquire flag_lock before running thread"""
        #flag needs to be aquired before call to this function so this is the first
        #flag update after the call
        self._exit_flag = False
        self.flag_lock.release()

        while True:
            print(self.name)
            time.sleep(0.5)
            if self._exit_flag:
                break

    def stop_thread(self):
        self.flag_lock.acquire()
        self._exit_flag = True
        self.flag_lock.release()

    def __str__(self):
        return 'class/object description'

    def get_new_frames(self):
        """ returns all frames since last call """
        return None


import scipy.io as sio
import cv2
import numpy as np

class Stereo_Camera_test():
    def generate_image_and_depth(self, depth_filename = './Peripheral_Communication/example_inputs/150_depth.mat',
    im_filename = './Peripheral_Communication/example_inputs/150_im.png'):
        m = sio.loadmat(depth_filename)
        depth = m['d']
        print(depth)
        image = cv2.imread(im_filename)
        return image, depth

    def get_image_and_depth(self):
        # Create a Camera object
        zed = sl.Camera()

        # Create a InitParameters object and set configuration parameters
        init_params = sl.InitParameters()
        init_params.camera_resolution = sl.RESOLUTION.RESOLUTION_HD720  # Use HD720 video mode (default fps: 60)
        # Use a right-handed Y-up coordinate system
        init_params.coordinate_system = sl.COORDINATE_SYSTEM.COORDINATE_SYSTEM_RIGHT_HANDED_Y_UP
        init_params.coordinate_units = sl.UNIT.UNIT_METER  # Set units in meters

        # Open the camera
        err = zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            exit(1)

        # Create and set RuntimeParameters after opening the camera
        runtime_parameters = sl.RuntimeParameters()
        runtime_parameters.sensing_mode = sl.SENSING_MODE.SENSING_MODE_STANDARD  # Use STANDARD sensing mode

        # Capture 50 images and depth, then stop
        i = 0
        image = sl.Mat()
        depth = sl.Mat()
        point_cloud = sl.Mat()

        while i < 1:
            # A new image is available if grab() returns SUCCESS
            if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                zed.retrieve_image(image, sl.VIEW.VIEW_LEFT)
                # Retrieve depth map. Depth is aligned on the left image
                zed.retrieve_measure(depth, sl.MEASURE.MEASURE_DEPTH)
                # Retrieve colored point cloud. Point cloud is aligned on the left image.
                zed.retrieve_measure(point_cloud, sl.MEASURE.MEASURE_XYZRGBA)

                # Get and print distance value in mm at the center of the image
                # We measure the distance camera - object using Euclidean distance
                x = round(image.get_width() / 2)
                y = round(image.get_height() / 2)
                err, point_cloud_value = point_cloud.get_value(x, y)

                distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
                                     point_cloud_value[1] * point_cloud_value[1] +
                                     point_cloud_value[2] * point_cloud_value[2])

                if not np.isnan(distance) and not np.isinf(distance):
                    distance = round(distance)
                    print("Distance to Camera at ({0}, {1}): {2} mm\n".format(x, y, distance))
                    # Increment the loop
                    i = i + 1
                else:
                    print("Can't estimate distance at this position, move the camera\n")
                sys.stdout.flush()

        # Close the camera
        zed.close()
