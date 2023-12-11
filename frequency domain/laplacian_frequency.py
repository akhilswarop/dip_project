
import cv2
import os
import numpy as np

# Input and output folder paths
input_root_folder = 'Data'
output_root_folder = 'laplacian_frequency_Images/'

# Ensure the output folder exists; create it if not
if not os.path.exists(output_root_folder):
    os.makedirs(output_root_folder)

# Function to perform Laplacian frequency domain filtering on a single image
def perform_laplacian_frequency(input_path, output_path):
    import cv2
    import numpy as np

    # Open and normalize the image
    f = cv2.imread(input_path)
    f = f / 255

    # Split the color image into channels
    R, G, B = cv2.split(f)

    # Transform each channel into the frequency domain
    F_R = np.fft.fftshift(np.fft.fft2(R))
    F_G = np.fft.fftshift(np.fft.fft2(G))
    F_B = np.fft.fftshift(np.fft.fft2(B))

    # Laplacian Filter
    P, Q = F_R.shape
    H = np.zeros((P, Q), dtype=np.float32)
    for u in range(P):
        for v in range(Q):
            H[u, v] = -4 * np.pi * np.pi * ((u - P / 2) ** 2 + (v - Q / 2) ** 2)

    # Apply Laplacian filter to each channel separately
    Lap_R = H * F_R
    Lap_G = H * F_G
    Lap_B = H * F_B

    # Combine the Laplacian-filtered channels back into a color image
    Lap_filtered_image = cv2.merge((np.real(np.fft.ifft2(Lap_R)), np.real(np.fft.ifft2(Lap_G)), np.real(np.fft.ifft2(Lap_B))))

    # Convert the Laplacian Image value into range [-1, 1]
    OldRange = np.max(Lap_filtered_image) - np.min(Lap_filtered_image)
    NewRange = 1 - -1
    LapScaled = (((Lap_filtered_image - np.min(Lap_filtered_image)) * NewRange) / OldRange) + -1

    # Image enhancement
    c = -1
    g = f + c * LapScaled
    g = np.clip(g, 0, 1)

    cv2.imwrite(output_path, (g * 255).astype(np.uint8))

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

                # Perform the Laplacian frequency transformation on the image
                perform_laplacian_frequency(input_path, output_path)

# Print a message when processing is complete
print("Laplacian frequency complete. Transformed images are saved in the output folder.")
