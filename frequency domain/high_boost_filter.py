import cv2
import os
import numpy as np

def highBoostFilteringFrequencyDomain(image, boost_factor):
    # Compute the 2D FFT of the image
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

    # Create a filter in the frequency domain
    rows, cols = image.shape
    filter = np.zeros((rows, cols), dtype=complex)
    center_row, center_col = rows // 2, cols // 2
    filter[center_row, center_col] = 1  # DC component
    filter = 1 + boost_factor * (filter - 1)

    # Apply the filter to the FFT of the image
    filtered_image = fshift * filter
    filtered_image = np.fft.ifftshift(filtered_image)
    filtered_image = np.fft.ifft2(filtered_image)
    filtered_image = np.abs(filtered_image)

    return filtered_image

input_root_folder = 'Data'
output_root_folder = 'High Boost Filtered Images'
boost_factor = 2.0

if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

for folder_name in os.listdir(input_root_folder):
    folder_path = os.path.join(input_root_folder, folder_name)

    if os.path.isdir(folder_path):
        output_folder = os.path.join(output_root_folder, folder_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)

                img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)  # Load the image in grayscale
                output = highBoostFilteringFrequencyDomain(img, boost_factor)

                cv2.imwrite(output_path, output)

print("High-boost filtering in the frequency domain complete. Processed images are saved in the output folder.")