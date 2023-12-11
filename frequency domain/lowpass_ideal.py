# low_pass_filter.py
import cv2
import numpy as np
import os

def apply_low_pass_filter(input_path, output_path, D0=50):
    f = cv2.imread(input_path, 0)
    F = np.fft.fft2(f)
    Fshift = np.fft.fftshift(F)

    M, N = f.shape
    H = np.zeros((M, N), dtype=np.float32)
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
            if D <= D0:
                H[u, v] = 1

    Gshift = Fshift * H
    G = np.fft.ifftshift(Gshift)
    g = np.abs(np.fft.ifft2(G))

    cv2.imwrite(output_path, g)

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'Low_Pass_idealFiltered_Images/'

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
            if filename.endswith('.jpg') or filename.endswith('.png'):
                input_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)

                apply_low_pass_filter(input_path, output_path)

print("Low pass filtering complete. Filtered images are saved in", output_root_folder)