import cv2
import numpy as np

def integral_image(img):
    return cv2.integral(img)

def adaptive_thresholding(img, window_size, t):
    h, w = img.shape
    int_img = integral_image(img)

    result = img.copy()  # Make a copy to store the result

    for i in range(w):
        for j in range(h):
            x1 = max(0, i - window_size // 2)
            x2 = min(w - 1, i + window_size // 2)
            y1 = max(0, j - window_size // 2)
            y2 = min(h - 1, j + window_size // 2)

            count = (x2 - x1) * (y2 - y1)
            sum_region = int_img[y2+1, x2+1] - int_img[y2+1, x1] - int_img[y1, x2+1] + int_img[y1, x1]

            if img[j, i] * count <= sum_region * (100 - t) / 100:
                result[j, i] = 0
            else:
                result[j, i] = 255

    return result

# Example usage with your provided image path
image_path = 'Test Images/test_2.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

window_size = 11
threshold_percent = 10
result = adaptive_thresholding(img, window_size, threshold_percent)

cv2.imshow('Original Image', img)
cv2.imshow('Adaptive Thresholding', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
