import cv2
import os
import numpy as np

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Log_Transformed_Images/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform a logarithmic transformation on a single image
def perform_log_transformation(input_path, output_path):
    image = cv2.imread(input_path)

    # Ensure the image is in float32 format
    image_float = image.astype(np.float32)

    # Add a small constant to avoid taking the logarithm of zero
    epsilon = 1e-5
    image_float = image_float + epsilon

    # Apply the logarithmic transformation
    log_transformed_image = np.log1p(image_float)

    # Normalize pixel values to the range [0, 255]
    log_transformed_image = (log_transformed_image / np.max(log_transformed_image)) * 255.0

    # Convert to 8-bit unsigned integer (uint8)
    log_transformed_image = log_transformed_image.astype(np.uint8)

    # Save the log-transformed image
    cv2.imwrite(output_path, log_transformed_image)

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

                # Perform the logarithmic transformation on the image
                perform_log_transformation(input_path, output_path)

# Print a message when processing is complete
print("Logarithmic transformation complete. Transformed images are saved in the output folder.")
