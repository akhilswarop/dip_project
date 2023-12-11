import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Smoothed_Data/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform Gaussian smoothing on a single image
def perform_gaussian_smoothing(input_path, output_path, kernel_size):
    image = cv2.imread(input_path)

    # Apply Gaussian smoothing
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Save the smoothed image
    cv2.imwrite(output_path, smoothed_image)

# Kernel size for Gaussian smoothing (adjust as needed)
kernel_size = 5  # You can change this value

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
                output_path = os.path.join(output_folder, 'smoothed_' + filename)

                # Perform Gaussian smoothing on the image
                perform_gaussian_smoothing(input_path, output_path, kernel_size)

# Print a message when processing is complete
print("Gaussian smoothing complete. Smoothed images are saved in the output folder.")
