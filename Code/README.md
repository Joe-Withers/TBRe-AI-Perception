# Perception

## Object detection
Given an image (or set of images), the object detection class returns a list (of size: same number of images input) of dictionaries in the following format:

{'num_detections': \<number of detections\>, 
  
'detection_boxes': \<array of [x, y, x, y]\>, 

'detection_scores': \<array of class scores\>,
  
'detection_classes': \<array of detected classes\>}

and example could look like:

{'num_detections': 100, 

'detection_boxes': array([[0.57712954, 0.5932685 , 0.8702174 , 0.7669569 ], ..., [0.69693774, 0.01846744, 0.8642351 , 0.04963544]], dtype=float32), 

'detection_scores': array([0.68798035, ..., 0.03173359], dtype=float32), 

'detection_classes': array([1, ..., 1], dtype=uint8)}

## Depth detection

## Matching

## Triangulation
