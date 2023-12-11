import cv2

# Load the image in grayscale
image = cv2.imread('sample.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the block size for adaptive thresholding
block_size = 11  # Adjust the block size as needed

# Calculate the adaptive threshold using mean and standard deviation
adaptive_threshold = cv2.adaptiveThreshold(
    image,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    block_size,
    C=2  # Constant subtracted from the mean (adjust as needed)
)

# Display the original and adaptive thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Thresholded Image', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
