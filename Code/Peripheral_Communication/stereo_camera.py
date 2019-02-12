import time
from threading import Thread, Lock

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
