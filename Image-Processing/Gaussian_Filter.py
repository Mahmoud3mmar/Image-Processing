


import random
from tkinter import filedialog
from distutils.core import setup

import cv2
import numpy as np




from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.image import imread
import matplotlib.image as mpimg



def Gaussian_filter(filename):
	import cv2
	import numpy as np

	# Load the image using OpenCV
	image = cv2.imread(filename)

	# Convert the image to grayscale
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Create a Gaussian kernel with a specified size and standard deviation
	def gaussian_kernel(size, sigma):
		kernel = np.zeros((size, size))
		center = size // 2

		for x in range(size):
			for y in range(size):
				r = np.sqrt((x - center) ** 2 + (y - center) ** 2)
				kernel[x, y] = np.exp(-r ** 2 / (2 * sigma ** 2))

		return kernel / np.sum(kernel)

	# Apply the Gaussian filter to the image
	def gaussian_filter(image, kernel_size, sigma):
		# Pad the image with zeros to handle the edges
		padded_image = np.pad(image, kernel_size // 2, mode="constant")

		# Create the Gaussian kernel
		kernel = gaussian_kernel(kernel_size, sigma)

		# Create an empty output image
		filtered_image = np.zeros_like(image)

		# Iterate over the image and apply the filter
		for i in range(image.shape[0]):
			for j in range(image.shape[1]):
				filtered_image[i, j] = np.sum(padded_image[i:i + kernel_size, j:j + kernel_size] * kernel)

		return filtered_image

	# Call the Gaussian filter function with a kernel size of 10 and a standard deviation of 5.0
	filtered_image = gaussian_filter(gray_image, 10, 5.0)

	# Display the original and filtered images
	cv2.imshow("Original", gray_image)
	cv2.imshow("Filtered", filtered_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
