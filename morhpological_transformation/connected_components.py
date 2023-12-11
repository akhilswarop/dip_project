import imageio.v3 as iio
import ipympl
import matplotlib.pyplot as plt
import numpy as np
import skimage as ski

def connected_components(filename, sigma=1.0, t=0.5, connectivity=2):
    filename='Test Images/test_1.jpg'
    image = iio.imread(filename)
    gray_image = ski.color.rgb2gray(image)
    blurred_image = ski.filters.gaussian(gray_image, sigma=sigma)
    binary_mask = blurred_image < t
    labeled_image, count = ski.measure.label(binary_mask,
                                                 connectivity=connectivity, return_num=True)
    return labeled_image, count
labeled_image, count = connected_components('Test Images/test_1.jpg', sigma=1.0, t=0.5, connectivity=2)

print("Connected Components Count:", count)
plt.figure()
plt.imshow(labeled_image, cmap='nipy_spectral')
plt.colorbar()
plt.show()