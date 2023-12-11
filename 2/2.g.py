import numpy as np
import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'region growing/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)



def region_growing(image, seed,threshold):
    visited = np.zeros_like(image)
    h, w = image.shape[:2]
    region = np.zeros_like(image)

    stack = [seed]
    while stack:
        x, y = stack.pop()
        if 0 <= x < h and 0 <= y < w and not visited[x, y]:
            if abs(int(image[x, y]) - int(image[seed])) < threshold:  # Adjust threshold as needed
                region[x, y] = 255
                visited[x, y] = 1
                stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    return region

# Function to perform linear image negation on a single image
def perform_linear_negation(input_path, output_path):
    image = cv2.imread(input_path)


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Seed coordinates (starting point for region growing)
    seed_point = (100, 100)

    # Set the threshold for similarity
    threshold = 20  # Adjust as needed

    # Perform region growing
    result = region_growing(gray_image, seed_point,threshold)

    # Perform adaptive thresholding


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











