import cv2

# Load the image in grayscale
image = cv2.imread('sample.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
_, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image (Otsu)', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
