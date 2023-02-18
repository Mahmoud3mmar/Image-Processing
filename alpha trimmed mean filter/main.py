import numpy as np
import matplotlib.pyplot as plt

def alpha_trimmed_mean_filter(input_image, kernel_size, alpha):
    lower_bound = int(alpha * kernel_size * kernel_size / 2)
    upper_bound = kernel_size * kernel_size - lower_bound
    padded_image = np.pad(input_image, kernel_size//2, mode='reflect')
    output_image = np.zeros_like(input_image)
    for i in range(input_image.shape[0]):
        for j in range(input_image.shape[1]):
            window = padded_image[i:i+kernel_size, j:j+kernel_size]
            window.sort()
            output_image[i, j] = np.mean(window[lower_bound:upper_bound])
    return output_image

# Read an input image
input_image = plt.imread('Noisy-image-Gaussian-noise-with-mean-and-variance-0005.png')

filtered_image = alpha_trimmed_mean_filter(input_image, 3, 0.2)

plt.subplot(1, 2, 1)
plt.imshow(input_image)
plt.title('Input image')
plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title('Output image')
plt.show()
