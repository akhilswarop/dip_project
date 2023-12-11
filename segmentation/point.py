import cv2
import numpy as np
def perform_thresholding(input_path, output_path, threshold=127):

  image = cv2.imread(input_path)
  grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply point thresholding
  binary_image = np.where(grayscale > threshold, 255, 0)
  binary_image = binary_image.astype(np.uint8)

  # Display and save the processed image
  cv2.imshow("point Thresholded Image", binary_image)
  cv2.imwrite(output_path, binary_image)

  # Wait for key press
  cv2.waitKey(0)

# Example usage
input_path = "Test Images\test_1.jpg"
output_path = "Test Images\Output\leonal\point thresholded_image.jpg"

perform_thresholding(input_path, output_path)

print("Thresholded image saved:", output_path)
