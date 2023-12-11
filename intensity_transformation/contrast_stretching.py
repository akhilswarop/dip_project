import cv2
import os
import numpy as np

# Input and output folder paths
input_root_folder = 'Data/'
output_root_folder = 'Stretched_Data/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)


# Function to perform contrast stretching on a single image
def perform_contrast_stretching(input_path, output_path):
    image = cv2.imread(input_path)

    # Normalize pixel values to the range [0, 1]
    image_normalized = image / 255.0

    # Define the minimum and maximum desired intensity levels
    min_intensity = 0.1  # Adjust this value as needed
    max_intensity = 0.8  # Adjust this value as needed

    # Apply contrast stretching
    stretched_image = (image_normalized - min_intensity) / (max_intensity - min_intensity)

    # Ensure pixel values are in the valid range [0, 1]
    stretched_image = np.clip(stretched_image, 0, 1)

    # Scale pixel values back to [0, 255] and convert to uint8
    stretched_image = (stretched_image * 255.0).astype(np.uint8)

    # Save the stretched image
    cv2.imwrite(output_path, stretched_image)


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

                # Perform contrast stretching on the image
                perform_contrast_stretching(input_path, output_path)

# Print a message when processing is complete
print("Contrast stretching complete. Stretched images are saved in the output folder.")
