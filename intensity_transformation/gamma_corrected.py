import cv2
import os
import numpy as np

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Gamma_Corrected_Data/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)


# Function to perform gamma correction on a single image
def perform_gamma_correction(input_path, output_path, gamma):
    image = cv2.imread(input_path)

    # Normalize pixel values to the range [0, 1]
    image_normalized = image / 255.0

    # Apply gamma correction
    corrected_image = np.power(image_normalized, gamma) * 255.0

    # Ensure pixel values are in the valid range [0, 255]
    corrected_image = np.clip(corrected_image, 0, 255)

    # Convert to 8-bit unsigned integer (uint8)
    corrected_image = corrected_image.astype(np.uint8)

    # Save the gamma-corrected image
    cv2.imwrite(output_path, corrected_image)


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
                gamma_value = 0.7 # Modify this value as desired

                # Perform gamma correction on the image
                perform_gamma_correction(input_path, output_path, gamma_value)

# Print a message when processing is complete
print("Gamma correction complete. Corrected images are saved in the output folder.")
