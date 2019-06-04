from Peripheral_Communication.stereo_camera import Stereo_Camera, Stereo_Camera_test
import cv2
import sys
import glob
import re

if __name__ == "__main__":
    folder_name = 'D:/Joe/Documents/University/TBReAI/saved_ZED_images'
    nums = []
    for file in glob.glob(folder_name+'/*.png'):
        print(file)
        all = re.findall(r'[0-9]+',file)
        nums.append(int(all[0]))
    start_index = max(nums)

    s = Stereo_Camera_test()

    n_images = 1000
    for i in range(start_index+1, start_index+n_images+1):
        image, depth_map = s.get_image_and_depth()
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        sys.stdout.flush()
        cv2.imwrite(folder_name+'/'+str(i)+'.png', image)

    s.close_cam()
