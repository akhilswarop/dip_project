import cv2
import numpy as np


def perform_opening(input_path, output_path):

    image = cv2.imread(input_path)
    filter_size = (3, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filter_size)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply opening operation
    opened_image = cv2.morphologyEx(grayscale_image, cv2.MORPH_OPEN, kernel)

    # Save the processed image
    cv2.imwrite(output_path, opened_image)


def perform_closing(input_path, output_path):

    image = cv2.imread(input_path)
    filter_size = (3, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filter_size)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply closing operation
    closed_image = cv2.morphologyEx(grayscale_image, cv2.MORPH_CLOSE, kernel)

    # Save the processed image
    cv2.imwrite(output_path, closed_image)


# Example usage
input_path = "Test Images/test_1.jpg"
output_path_opening = "Test Images\Output\leonal\opening_result.jpg"
output_path_closing = "Test Images\Output\leonal\closing_result.jpg"

perform_opening(input_path, output_path_opening)
perform_closing(input_path, output_path_closing)

print("Opening result saved:", output_path_opening)
print("Closing result saved:", output_path_closing)
