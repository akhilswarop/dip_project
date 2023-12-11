import cv2
import numpy as np

def region_growing(image, seed, threshold):
    height, width = image.shape
    segmented = np.zeros_like(image)
    visited = np.zeros_like(image)
    
    # Queue for pixel coordinates
    queue = []
    queue.append(seed)

    seed_intensity = image[seed]

    while queue:
        current_pixel = queue.pop(0)
        x, y = current_pixel

        if visited[x, y] == 1:
            continue

        # Check if the pixel intensity is similar to the seed pixel
        if abs(int(image[x, y]) - int(seed_intensity)) < threshold:
            segmented[x, y] = 255
            visited[x, y] = 1

            # Add 4-connected neighbors to the queue
            if x > 0:
                queue.append((x - 1, y))
            if x < height - 1:
                queue.append((x + 1, y))
            if y > 0:
                queue.append((x, y - 1))
            if y < width - 1:
                queue.append((x, y + 1))

    return segmented

def perform_region_growing(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Choose a seed pixel (you can adjust this based on your image)
    seed = (160, 80)

    # Set the threshold for region growing
    threshold = 10  # Adjust this value based on your image

    # Apply region growing algorithm
    segmented_image = region_growing(image, seed, threshold)

    # Display the original and segmented images
    cv2.imshow('Original Image', image)
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)  # Wait for a key event
    cv2.destroyAllWindows()  # Close all OpenCV windows

    # Save the segmented image
    cv2.imwrite(output_path + '.jpg', segmented_image)

# Example usage
input_path = 'Test Images/test_1.jpg'
output_path = 'Test Images/Output/Hanish'
perform_region_growing(input_path, output_path)
