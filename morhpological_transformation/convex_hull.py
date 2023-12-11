import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image (assuming a binary image where objects are white on a black background)
image_path = 'sample.jpeg'
binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty image to draw the convex hull
convex_hull_image = np.zeros_like(binary_image)

# Iterate through contours and draw the convex hull
for contour in contours:
    hull = cv2.convexHull(contour)
    cv2.drawContours(convex_hull_image, [hull], 0, 255, thickness=cv2.FILLED)

# Display the original image and the convex hull image
plt.subplot(121), plt.imshow(binary_image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(convex_hull_image, cmap='gray')
plt.title('Convex Hull Image'), plt.xticks([]), plt.yticks([])

plt.show()
