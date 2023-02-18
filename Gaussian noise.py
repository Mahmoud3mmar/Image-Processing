import cv2
import numpy as np

# Load the image using OpenCV
image = cv2.imread("image.png")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Add Gaussian noise to the image
def add_gaussian_noise(image, mean, std):
  # Generate an array of random noise values with the same shape as the image
  noise = np.random.normal(mean, std, image.shape)

  # Add the noise to the image
  noisy_image = image + noise

  # Clip the values of the noisy image to the range [0, 255]
  for i in range(noisy_image.shape[0]):
    for j in range(noisy_image.shape[1]):
      if noisy_image[i,j] < 0:
        noisy_image[i,j] = 0
      elif noisy_image[i,j] > 255:
        noisy_image[i,j] = 255

  return noisy_image.astype(np.uint8)

# Call the add_gaussian_noise() function with a mean of 0 and a standard deviation of 200
noisy_image = add_gaussian_noise(gray_image, 0, 200)

# Display the original and noisy images
cv2.imshow("Original", gray_image)
cv2.imshow("Noisy", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
