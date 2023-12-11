import matplotlib.pyplot as plt
import numpy as np
import cv2

def custom_imread(file_path, grayscale=True):
    image = plt.imread(file_path)
    if grayscale:
        image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # Convert to grayscale manually
    return image.astype(np.uint8)

def custom_threshold(image, threshold):
    thresholded_image = (image > threshold) * 255
    return thresholded_image.astype(np.uint8)

def perform_image_processing(input_path, output_path):
    # Load image using custom function
    image = custom_imread(input_path)

    # Binarize the image using custom thresholding
    manual_threshold = 128  # Adjust threshold as needed
    binary_image = custom_threshold(image, manual_threshold)

    # Perform morphological closing to fill holes
    kernel_size = (22, 22)  # Adjust kernel size as needed
    kernel = np.ones(kernel_size, np.uint8)
    filled_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

    # Show original image, binary image, and filled image side-by-side
    fig, axs = plt.subplots(1, 2, figsize=(10, 10))
    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('Original')

    axs[1].imshow(filled_image, cmap='gray')
    axs[1].set_title('Filled')

    plt.show()

    # Save the filled image
    cv2.imwrite(output_path, filled_image)

# Example usage
input_path = r"Test Images/test_2.jpg"
output_path = r"Test Images/Output/Hanish"
perform_image_processing(input_path, output_path)