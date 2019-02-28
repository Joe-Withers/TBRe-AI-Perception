# TODO
## Peripheral communication
* write function to use the ZED sdk for reading the input.                                              \[pending\]
## Object detection
* wait for better training data                                                                         \[pending\]
* consider writing a canny edge cone detector as a back-up.                                             \[pending\]
## Depth detection
* function for detecting depth.                                                                         \[done\]
* function for generating ground truth inputs to test the depth detection function.                     \[pending\]
## 3D projection
* function for projecting 2D image coordinates to 3D coordinates using the depth from depth detection.  \[pending\]
* function for generating ground truths for testing this.                                               \[pending\]

# TBRe-AI-Perception
Uses stereo cameras to perceive relative cone locations.

# architecture
![alt text](https://github.com/Joe-Withers/TBRe-AI-Perception/blob/master/architecture.PNG)

# workflow
![alt text](https://github.com/Joe-Withers/TBRe-AI-Perception/blob/master/workflow.PNG)

Two alternative routes to get realtive 3d locations of cones. The green route uses the depth map from the stereo cameras, the red route matches between a pair of images and triangulates.

# dependencies
* Python 3
* Tensorflow 1.9 or later
* Tensorflows object-detection api
