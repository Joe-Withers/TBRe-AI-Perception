
from threading import Thread

class StereoCamera(Thread):
    def __init__(self, camera_name):
        Thread.__init__(self)
        print('initilise')

    def run(self):
        while True:
            print('get frames')

    def __str__(self):
        return 'class/object description'

    def get_new_frames(self):
        """ returns all frames since last call """
        return None
