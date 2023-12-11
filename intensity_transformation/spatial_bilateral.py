import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Bilateral_Filtered_Data/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform bilateral filtering on a single image
def perform_bilateral_filtering(input_path, output_path, diameter, sigma_color, sigma_space):
    image = cv2.imread(input_path)

    # Apply bilateral filtering
    filtered_image = cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)

    # Save the filtered image
    cv2.imwrite(output_path, filtered_image)

# Parameters for bilateral filtering (adjust as needed)
diameter =9          # Diameter of each pixel neighborhood
sigma_color = 75      # Filter sigma in the color space
sigma_space = 75      # Filter sigma in the coordinate space

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
                output_path = os.path.join(output_folder, 'bilateral_filtered_' + filename)

                # Perform bilateral filtering on the image
                perform_bilateral_filtering(input_path, output_path, diameter, sigma_color, sigma_space)

# Print a message when processing is complete
print("Bilateral filtering complete. Filtered images are saved in the output folder.")
