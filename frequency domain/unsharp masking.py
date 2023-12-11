import cv2
import numpy as np
from PIL import Image
from IPython.display import display

# Load image
in_img = cv2.imread("/data.jpeg.jpg", cv2.IMREAD_COLOR)

# Display original image (optional)
display(Image.fromarray(cv2.cvtColor(in_img, cv2.COLOR_BGR2RGB)))

# Convert the image to grayscale
gray_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)

# Gaussian blur manually
blurred = np.zeros_like(gray_img, dtype=np.float32)
cv2.GaussianBlur(gray_img.astype(np.float32), (0, 0), 5.3, dst=blurred, borderType=cv2.BORDER_REFLECT)

# Unsharp masking manually
sharpened = cv2.addWeighted(gray_img.astype(np.float32), 1.0 + 5.3, blurred, -5.3, 0)

# Convert back to uint8 for displaying
sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

# Display sharpened image (optional)
display(Image.fromarray(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)))