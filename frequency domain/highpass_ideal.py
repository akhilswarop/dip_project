# high_pass_filter_rgb.py
import cv2
import numpy as np
import os


def apply_high_pass_filter_rgb(input_path, output_path, D0=50):
    # Read the image in color
    image = cv2.imread(input_path)

    # Split the image into its R, G, B channels
    b, g, r = cv2.split(image)

    # Function to apply the high pass filter to a single channel
    def high_pass_channel(channel):
        F = np.fft.fft2(channel)
        Fshift = np.fft.fftshift(F)

        M, N = channel.shape
        H = np.ones((M, N), dtype=np.float32)
        for u in range(M):
            for v in range(N):
                D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
                if D <= D0:
                    H[u, v] = 0

        Gshift = Fshift * H
        G = np.fft.ifftshift(Gshift)
        g = np.abs(np.fft.ifft2(G))
        return g

    # Apply the high pass filter to each channel
    b_filtered = high_pass_channel(b)
    g_filtered = high_pass_channel(g)
    r_filtered = high_pass_channel(r)

    # Merge the filtered channels back into an RGB image
    filtered_image = cv2.merge([b_filtered, g_filtered, r_filtered])

    # Convert the floating point image to 8-bit unsigned integer
    filtered_image = cv2.convertScaleAbs(filtered_image)

    # Save the filtered image
    cv2.imwrite(output_path, filtered_image)


# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'High_Pass_idealFiltered_Images_RGB/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Process images
for folder_name in os.listdir(input_root_folder):
    folder_path = os.path.join(input_root_folder, folder_name)
    if os.path.isdir(folder_path):
        output_folder = os.path.join(output_root_folder, folder_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.png')):
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)

                apply_high_pass_filter_rgb(input_path, output_path)

print("High pass filtering complete. Filtered images are saved in", output_root_folder)