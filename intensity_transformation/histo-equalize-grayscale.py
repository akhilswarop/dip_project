import cv2
import numpy as np
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Histogram_Processed_Images/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform histogram equalization on a single image
def perform_histogram_equalization(input_path, output_path):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Save the histogram-equalized image
    cv2.imwrite(output_path, equalized_image)

# Function to perform histogram matching on a single image
def perform_histogram_matching(input_path, output_path, reference_path):
    input_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Read the input image in grayscale
    reference_image = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)  # Read the reference image in grayscale

    # Perform histogram matching
    matched_image = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(input_image)

    # Save the histogram-matched image
    cv2.imwrite(output_path, matched_image)

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
                output_path_equalization = os.path.join(output_folder, 'equalized_' + filename)
                output_path_matching = os.path.join(output_folder, 'matched_' + filename)

                # Perform histogram equalization on the image
                perform_histogram_equalization(input_path, output_path_equalization)

                # Specify a reference image for histogram matching (you can replace this with your reference image)
                reference_image_path = 'Reference_color'

                # Perform histogram matching on the image using the reference image
                perform_histogram_matching(input_path, output_path_matching, reference_image_path)

# Print a message when processing is complete
print("Histogram operations complete. Processed images are saved in the output folder.")
