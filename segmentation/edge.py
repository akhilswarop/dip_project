import cv2


def perform_edge_detection(input_path, output_path):

    # Read the image
    img = cv2.imread(input_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply Canny edge detection algorithm
    edges = cv2.Canny(blur, 100, 200)

    # Save the edges image
    cv2.imwrite(output_path, edges)


# Usage example
input_path = "image.jpg"
output_path = "edges.jpg"

perform_edge_detection(input_path, output_path)

print("Edge detection completed successfully!")
