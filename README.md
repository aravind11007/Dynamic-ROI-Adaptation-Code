# Dynamic ROI Adaptation Code

This repository provides an implementation of **Dynamic Region of Interest (ROI) Adaptation** for video-based applications. The required dataset can be downloaded from the [UBFC-rPPG Dataset](https://sites.google.com/view/ybenezeth/ubfcrppg).  
For labeling, please use the [LabelMe software](https://github.com/wkentaro/labelme).  
A sample of labeled data is included in the `sample` folder for reference.

## Steps for Running the Code

### 1. Preparing the Data
- Place the images and their corresponding coordinates (generated using the LabelMe software) in a folder.

### 2. Mask Creation
- Open the `mask_creation.ipynb` file.
- Specify the folder path containing the images and their coordinates to generate the masks.

### 3. Data Augmentation
- To augment the images and their masks:
  - Open and run the `augment_data.ipynb` file.
  - Provide the folder paths for the images and their corresponding masks.

### 4. Model Training
- Once the data augmentation is complete:
  - Use the `training_vgg.ipynb` file to train the model.

### 5. Model Testing on Live Video
- To test the trained model on a live video stream:
  - Run the `testing_live_stream.ipynb` file.

### 6. Heart Rate Estimation
- For heart rate estimation:
  - Execute the `testing_live_stream.ipynb` file as described above.

## Notes
- This implementation works seamlessly with the provided dataset and LabelMe tool.
- Ensure all paths are configured correctly in the `.ipynb` files before execution.
