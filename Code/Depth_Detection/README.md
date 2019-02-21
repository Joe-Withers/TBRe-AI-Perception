# Depth detection

## TODO:

### Implement a function in the module 'generate_depth_input.py' 
This should include a function that generates the input information for the get_depth function in the Depth_Detector class. Note this is for testing purposes so you can just hard code some example depth_maps and object_dicts.
*Note: refer to the readme in 'code/' folder for more detail on the format of output_dict returned from the object detector.

### Implement the get_depth function.

This function will be passed a list of object_dict.
For each object_dict, extract its bounding box measurements. Denormalize them, to give you the top left and bottom right coordinates. Then you can simply extract the section from the depth map corresponding to the area inside the bounding box and use an appropriate method for assuming the depth of the cone (e.g. take the nearest depth within a standard deviation of N). Bear in mind this code will be running real time so avoid loops as much as you can. For extracting the coordinates of the depth map inside the bounding box look and using slicing with numpy (https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm ).

### finally 
Test the get_depth function using the function in generate_depth_input.py.
You can do this by adding the code below at the bottom of the depth_detection.py module.
if \_\_name\_\_ == "\_\_main\_\_":
	\<code to test the function\>

	
