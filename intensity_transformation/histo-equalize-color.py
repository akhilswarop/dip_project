import cv2
import os

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Color_Histogram_Matched_Images/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to determine the class of an image based on its folder structure
def get_image_class(image_path):
    # Extract the class name from the folder structure
    class_name = os.path.basename(os.path.dirname(image_path))
    return class_name

# Function to perform histogram matching on a single color image
def perform_color_histogram_matching(input_path, output_path, class_name, reference_root_folder):
    # Determine the path to the reference image for the corresponding class
    reference_folder = os.path.join(reference_root_folder, class_name)
    reference_image_path = os.path.join(reference_folder, 'reference_image.jpg')

    input_image = cv2.imread(input_path)
    reference_image = cv2.imread(reference_image_path)

    # Split the input and reference images into their color channels
    input_blue, input_green, input_red = cv2.split(input_image)
    reference_blue, reference_green, reference_red = cv2.split(reference_image)

    # Apply histogram matching to each color channel separately
    matched_blue = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(input_blue)
    matched_green = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(input_green)
    matched_red = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(input_red)

    # Merge the matched channels back into the color image
    matched_image = cv2.merge([matched_blue, matched_green, matched_red])

    # Save the histogram-matched color image
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
                output_path = os.path.join(output_folder, 'matched_' + filename)

                # Determine the class of the input image
                class_name = get_image_class(input_path)

                # Specify the root folder containing reference images
                reference_root_folder = 'Reference_color'

                # Perform histogram matching on the color image using the reference image for the class
                perform_color_histogram_matching(input_path, output_path, class_name, reference_root_folder)

# Print a message when processing is complete
print("Color histogram matching complete. Processed images are saved in the output folder.")
