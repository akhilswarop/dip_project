import numpy as np
import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Region-Based Segmentation (Region Splitting and Merging Algorithm)/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)


def split_and_merge(image, threshold, min_region_size=10):
    h, w = image.shape[:2]

    stack = [(0, 0, h, w)]  # Initialize stack with the whole image coordinates

    while stack:
        top, left, bottom, right = stack.pop()

        region = image[top:bottom, left:right]

        if region.shape[0] > min_region_size and region.shape[1] > min_region_size:
            mean_value = np.mean(region)

            if np.any(np.abs(region - mean_value) > threshold):
                mid_vertical = (top + bottom) // 2
                mid_horizontal = (left + right) // 2

                stack.extend([
                    (top, left, mid_vertical, mid_horizontal),
                    (top, mid_horizontal, mid_vertical, right),
                    (mid_vertical, left, bottom, mid_horizontal),
                    (mid_vertical, mid_horizontal, bottom, right)
                ])
            else:
                image[top:bottom, left:right] = mean_value  # Merge the region

    return image



def perform_linear_negation(input_path, output_path):
    image = cv2.imread(input_path)


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Seed coordinates (starting point for region growing)
    splitting_threshold = 50  # Adjust as needed

    splitting_threshold = 50  # Adjust as needed

    # Set the minimum region size to prevent infinite recursion
    min_region_size = 10  # Adjust as needed

    # Perform region splitting and merging
    result= split_and_merge(gray_image.copy(), splitting_threshold, min_region_size)

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











