import cv2
import os
import numpy as np

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Piecewise_Linear_Transformed_Images/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform a piecewise-linear transformation on a single image
def perform_piecewise_linear_transformation(input_path, output_path):
    image = cv2.imread(input_path)

    # Define the piecewise-linear transformation curve
    def piecewise_linear_mapping(x):
        if x < 128:
            return int(2 * x)
        else:
            return int((x - 128) * 1.5 + 255 - 128)

    # Apply the piecewise-linear transformation element-wise
    transformed_image = np.vectorize(piecewise_linear_mapping)(image)

    # Ensure pixel values are in the valid range [0, 255]
    transformed_image = np.clip(transformed_image, 0, 255)

    # Convert to 8-bit unsigned integer (uint8)
    transformed_image = transformed_image.astype(np.uint8)

    # Save the piecewise-linear transformed image
    cv2.imwrite(output_path, transformed_image)

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
                perform_piecewise_linear_transformation(input_path, output_path)

# Print a message when processing is complete
print("Piecewise-linear transformation complete. Transformed images are saved in the output folder.")
