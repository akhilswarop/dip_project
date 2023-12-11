import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Median_Filtered_Data/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform median filtering on a single image
def perform_median_filtering(input_path, output_path, kernel_size):
    image = cv2.imread(input_path)

    # Apply median filtering
    median_filtered_image = cv2.medianBlur(image, kernel_size)

    # Save the median-filtered image
    cv2.imwrite(output_path, median_filtered_image)

# Kernel size for median filtering (adjust as needed)
kernel_size = 3  # You can change this value

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
                output_path = os.path.join(output_folder, 'median_filtered_' + filename)

                # Perform median filtering on the image
                perform_median_filtering(input_path, output_path, kernel_size)

# Print a message when processing is complete
print("Median filtering complete. Median-filtered images are saved in the output folder.")
