import cv2
import numpy as np

image = cv2.imread('Test Images/test_1.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)
erosion_result = cv2.erode(image, kernel, iterations=1)

cv2.imshow('Original', image)
cv2.imshow('Erosion', erosion_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
