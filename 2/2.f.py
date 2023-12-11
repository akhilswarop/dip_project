import numpy as np
import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Adaptive Thresholding using Moving Averages/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform linear image negation on a single image
def perform_linear_negation(input_path, output_path):
    image = cv2.imread(input_path)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur for smoothing
    image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)

    # Ensure the correct data type
    image_blur = image_blur.astype(np.uint8)

    # Perform adaptive thresholding
    result = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    cv2.imwrite(output_path, result)

# Recursively process images in subfolders from 'A' to 'Z'
for folder_name in os.listdir(input_root_folder):
    folder_path = os.path.join(input_root_folder, folder_name)

    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Create a corresponding output folder
        output_folder = os.path.join(output_root_folder, folder_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Process images in the current subfolder
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):  # Filter for image files
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)

                # Perform the piecewise-linear transformation on the image
                perform_linear_negation(input_path, output_path)











