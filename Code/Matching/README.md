# Matching

### Implement a function in the module 'generate_matching_input.py' 
This should include a function that generates the input information for the match_objects function in the Matching class. Note this is for testing purposes so you can just hard code some example object_dicts for some images for testing purposes. Just think about what it is that you are trying to test.

*Note: refer to the readme in 'code/' folder for more detail on the format of output_dict returned from the object detector.*

### Implement the match_objects function.

This function will be passed a two object_dicts for each stereo image (i.e. the same time from different positions).
For each object_dict, extract its bounding box measurements. Denormalize them, to give you the top left and bottom right coordinates. Then you can simply extract the section from the image (respectively) corresponding to the area inside the bounding box. This will give you a list of patches for each image. Next compare the patches between the two images using SSD and use an appropriate matching technique. Bear in mind this code will be running real time so try to avoid loops as much as you can.

For extracting the patches of the images inside the bounding box look and using slicing with numpy (https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm ). 
For matching these patches a useful resource is (\<soon to come\>).

Just using SSD, to calculate the error between patches will not be suffient for the inputs this will get. For example the object detection may draw a bounding box of size 100x100 around cone1 in image1 and a box of size 120x100 around cone1 in image2. __Do NOT resize the images__ (or at least if you are going to don't do it by much); say for example, you where comparing cone1 in image1 which is really close to the camera with a bounding box of size 170x150 against cone2 in image2 which is very far away from the comera with bounding box of size 10x12, if you resize the images to match and perform SSD then the error may be respectably low, when in reality the error should be very high. Instead of resizing consider a sliding window approach (but again this is to run in real time so be a bit clever about how you do it).

### finally 
Test the match_objects function using the function in generate_matching_input.py.
You can do this by adding the code below at the bottom of the matching.py module.
if \_\_name\_\_ == "\_\_main\_\_":
	\<code to test the function\>
