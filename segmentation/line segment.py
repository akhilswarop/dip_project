import cv2
import numpy as np


def perform_line_thresholding(input_path, output_path):

    # Read the input image
    image = cv2.imread(input_path)

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    #This step detects edges in the image.
    edges = cv2.Canny(grayscale, 50, 150)

    # Apply Hough transform to detect lines
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # Create a blank image for drawing lines
    line_image = np.copy(image)

    # Draw the detected lines on the output image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Save the output image
    cv2.imwrite(output_path, line_image)


# Example usage
input_path = "Test Images/test_1.jpg"
output_path = "Test Images\Output\leonal/thresholded_lines.jpg"

perform_line_thresholding(input_path, output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
