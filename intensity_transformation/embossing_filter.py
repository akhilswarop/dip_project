import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# Input and output folder paths
input_root_folder = 'download.jpeg'
output_root_folder = 'Embossed_Data/'


image = cv2.imread(input_root_folder)

# Define the embossing kernel
kernel = np.array([[-2, -1, 0],
                   [-1,  1, 1],
                   [ 0,  1, 2]])
kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9,  1/9, 1/9],
                   [1/9,  1/9, 1/9]])
# Apply convolution to perform embossing
laplacian_image = cv2.filter2D(image, -1, kernel)

# Save the embossed image
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(laplacian_image),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
# Print a message when processing is complete
print("Embossing complete. Embossed images are saved in the output folder.")
