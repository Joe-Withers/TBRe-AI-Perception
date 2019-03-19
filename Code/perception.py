from threading import Thread, Lock
import time
from Peripheral_Communication.stereo_camera import Stereo_Camera, Stereo_Camera_test
from Object_Detection.object_detector import Object_Detector
from Depth_Detection.depth_detection import Object_Depth_Detector
from Projection.projection import Projection
import os
import numpy as np

class Perception(Thread):
    """ main class for perception, to be called from 'mapping and localisation' to aquire
    3D cone locations """
    def __init__(self, threadID, name):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        #using a lock to stop the flag from being updated at same time
        self.flag_lock = Lock()

        self.flag_lock.acquire()
        self._exit_flag = False
        self.flag_lock.release()

        # set up stereo camera
        self.stereo_cam1 = Stereo_Camera(0,'cam1')

        # #set up object detector
        # model_name = ''
        # frozen_graph_name = ''
        # labels = ''
        # self.cone_detector = Object_Detector(model_name, frozen_graph_name, labels, debug_mode = False)

        #set up matcher
        #self.matcher = Object_Matcher()

        #set up depth detector
        #self.depth_detector = Object_Depth_Detector()

        #set up triangulater
        #self.triangulator = Triangulation()

    def __str__(self):
        return 'class description'

    def stop_thread(self):
        self.flag_lock.acquire()
        self._exit_flag = True
        self.flag_lock.release()

    def run(self):
        """ perceives cones and publishes it to a topic (on a loop)
        Note: Always acquire flag_lock before running thread"""
        #flag needs to be aquired before call to this function so this is the first
        #flag update after the call
        self._exit_flag = False
        self.flag_lock.release()

        self.stereo_cam1.flag_lock.acquire()
        self.stereo_cam1.start() #start loop for reading frames
        while True:
            # step 1: get frames since last loop
            frames = self.stereo_cam1.get_new_frames()

            # step 2: detect cones in frames
            #output_dicts = self.cone_detector.detect_objects(frames)

            # step 3: match cones
            #self.matcher

            # step 4: find depth of cones
            #self.depth_detector

            #Note: step 3 and 4 can probably be done in parallel

            # step 5: triangulate cones
            #self.triangulator

            #TODO: publish to topic on ROS

            time.sleep(1)
            print(self.name)
            if self._exit_flag:
                self.stereo_cam1.stop_thread()#stop loop for reading camera frames
                break

def format_output_dicts(output_dicts):
    images_boxes = [output_dict["detection_boxes"] for output_dict in output_dicts]
    return images_boxes

class Perception_test():
    """ use this class to test the various modules together """
    def __init__(self, model_name, frozen_graph_name):
        self.cone_detector = Object_Detector(model_name, frozen_graph_name, labels, debug_mode = True)
        self.depth_detector = Object_Depth_Detector()
        self.projector = Projection()

    def run_images(self, images, depth_maps):

        output_dicts = self.cone_detector.detect_objects(images)
        images_boxes = format_output_dicts(output_dicts)
        depths = [self.depth_detector.get_depth(boxes, depth_map) for boxes, depth_map in zip(images_boxes, depth_maps)]
        relative_coordinates = [self.projector.project_to_3d(boxes, depth, image.shape) for boxes, depth, image in zip(images_boxes, depths, images)]
        print('relative_coordinates:',relative_coordinates)

# if __name__ == "__main__":
#     p = Perception(0,'main_percepter')
#     p.flag_lock.acquire()
#     p.start()
#     time.sleep(5)
#     p.stop_thread()
#     print('exited')

if __name__ == "__main__":
    model_name = './Object_Detection/cones_graph'
    frozen_graph_name = '/frozen_inference_graph.pb'
    labels = os.path.join('./Object_Detection/data', 'object-detection.pbtxt')
    p = Perception_test(model_name, frozen_graph_name)
    s = Stereo_Camera_test()

    image, depth_map = s.generate_image_and_depth()
    images = np.expand_dims(np.array(image), axis=0)
    depth_maps = np.expand_dims(np.array(depth_map), axis=0)
    p.run_images(images, depth_maps)
