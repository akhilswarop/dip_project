from PIL import Image
import numpy as np
import os



def apply_high_pass_filter(input_path, output_path, D0, k1, k2):
    # Read the original image
    img = Image.open(input_path)


    img_array = np.array(img)
    npFFT_R = np.fft.fft2(img_array[:, :, 0])
    npFFT_G = np.fft.fft2(img_array[:, :, 1])
    npFFT_B = np.fft.fft2(img_array[:, :, 2])


    (P, Q) = npFFT_R.shape
    H = np.zeros((P, Q))
    for u in range(P):
        for v in range(Q):
            H[u, v] = 1.0 - np.exp(-((u - P / 2.0) ** 2 + (v - Q / 2.0) ** 2) / (2 * (D0 ** 2)))

    HFEfilt = k1 + k2 * H

    # Apply HFE filter to each color channel
    HFE_R = HFEfilt * npFFT_R
    HFE_G = HFEfilt * npFFT_G
    HFE_B = HFEfilt * npFFT_B

    def ifft2d(image):
        ifftcols = np.array([np.fft.ifft(row) for row in image]).transpose()
        return np.array([np.fft.ifft(row) for row in ifftcols]).transpose()


    HFEfinal_R = np.abs(ifft2d(HFE_R))
    HFEfinal_G = np.abs(ifft2d(HFE_G))
    HFEfinal_B = np.abs(ifft2d(HFE_B))


    processed_image = np.stack((HFEfinal_R, HFEfinal_G, HFEfinal_B), axis=-1)


    processed_image = np.clip(processed_image, 0, 255)


    processed_image = processed_image.astype('uint8')


    processed_image = Image.fromarray(processed_image, 'RGB')


    processed_image.save(output_path)

# Define high-frequency emphasis filter parameters
filter_params = [
    {'name': 'Filter1', 'D0': 40, 'k1': 0.5, 'k2': 0.75},
    {'name': 'Filter2', 'D0': 50, 'k1': 0.6, 'k2': 0.7},
    # Add more filter parameter sets as needed
]

# Input and output folder paths
input_root_folder = 'data'  # Parent folder with subfolders
output_root_folder = 'High Frequency Emphasis Images'  # Output folder

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Process images in the input folder using different high-frequency emphasis filters
for filter_param in filter_params:
    filter_name = filter_param['name']
    filter_output_folder = os.path.join(output_root_folder, filter_name)

    if not os.path.exists(filter_output_folder):
        os.makedirs(filter_output_folder)

    for folder_name in os.listdir(input_root_folder):
        folder_path = os.path.join(input_root_folder, folder_name)

        if os.path.isdir(folder_path):
            # Create a corresponding output folder
            output_folder = os.path.join(filter_output_folder, folder_name)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            for filename in os.listdir(folder_path):
                if filename.endswith('.jpg') or filename.endswith('.png'):  # Filter for image files
                    input_path = os.path.join(folder_path, filename)
                    output_path = os.path.join(output_folder, filename)

                    # Apply the high-pass Gaussian filter with high-frequency emphasis
                    D0 = filter_param['D0']
                    k1 = filter_param['k1']
                    k2 = filter_param['k2']
                    apply_high_pass_filter(input_path, output_path, D0, k1, k2)

# Print a message when processing is complete
print("High-frequency emphasis complete. Processed images are saved in the output folder.")
