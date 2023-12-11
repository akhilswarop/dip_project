import numpy as np
import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = ' Adaptive Thresholding using Histogram Analysis/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform linear image negation on a single image
def perform_linear_negation(input_path, output_path):
    image = cv2.imread(input_path)

    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Negate the image by subtracting it from 255
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Perform adaptive thresholding
    threshold = np.interp(0.7, cdf_normalized / cdf_normalized.max(), bins[:-1])
    result = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
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











