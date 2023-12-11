import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'sample.jpeg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply GaussianBlur to reduce noise and help edge detection
blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)

# Apply Canny edge detector
edges = cv2.Canny(blurred_image, 50, 150)

# Display the results
plt.subplot(121), plt.imshow(original_image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
