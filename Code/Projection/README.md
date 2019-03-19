# 3D projection

For each object detected (i.e. each cone). Simply use the 2d location on the image plane, the focal length of the camera, and the depth of the object to calculate the 3d point.

Something along the lines of:
for each object:
	3d_point = (2d_location_relative_to_center * depth)/focal_length
*__check this__ but this is the general idea. Note: the 2d location is in pixels, but we want the 3d_point in some distance measurement.*