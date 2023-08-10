

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




def Adaptive(filename):
	import numpy as np
	from PIL import Image

	# Load the image and convert it to grayscale
	image = Image.open(filename).convert('L')

	# Convert the image to a numpy array
	image_array = np.array(image)

	# Define the size of the filter kernel (e.g. 3x3)
	kernel_size = 3

	# Create an output image with the same size as the input image
	filtered_image = np.zeros_like(image_array)

	# Iterate over the image and apply the median filter to each pixel
	for i in range(image_array.shape[0]):
		for j in range(image_array.shape[1]):
			# Select the neighborhood around the pixel
			i_min = max(i - kernel_size // 2, 0)
			i_max = min(i + kernel_size // 2 + 1, image_array.shape[0])
			j_min = max(j - kernel_size // 2, 0)
			j_max = min(j + kernel_size // 2 + 1, image_array.shape[1])
			neighborhood = image_array[i_min:i_max, j_min:j_max]

			# Compute the median value in the neighborhood
			filtered_value = np.median(neighborhood)

			# Set the filtered value for the pixel in the output image
			filtered_image[i, j] = filtered_value

	# Create an image from the filtered image array
	filtered_image = Image.fromarray(np.uint8(filtered_image))

	# Save the image to a file
	filtered_image.save('filtered_image.jpg')

	# Open the image
	image = Image.open('filtered_image.jpg')
	image.show()
