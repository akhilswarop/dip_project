import cv2
import os
import numpy as np

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Sharpened_Data/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform sharpening using a spatial filter on a single image
def perform_sharpening(input_path, output_path):
    image = cv2.imread(input_path)

    # Define the sharpening kernel (Laplacian )
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])

    # Apply convolution to sharpen the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # Save the sharpened image
    cv2.imwrite(output_path, sharpened_image)

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

                # Perform sharpening on the image
                perform_sharpening(input_path, output_path)

# Print a message when processing is complete
print("Sharpening complete. Sharpened images are saved in the output folder.")
