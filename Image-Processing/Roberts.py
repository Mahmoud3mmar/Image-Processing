



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



def Roberts(filename):

	# Load the image and convert it to grayscale
	image = Image.open(filename).convert('L')

	# Convert the image to a numpy array
	image_array = np.array(image)

	# Define the Roberts cross-gradient operators
	roberts_x = np.array([[1, 0], [0, -1]])
	roberts_y = np.array([[0, 1], [-1, 0]])

	# Create empty arrays to store the gradient in the x and y directions
	gradient_x = np.zeros_like(image_array)
	gradient_y = np.zeros_like(image_array)

	# Iterate over the image and compute the gradient in the x and y directions
	for i in range(1, image_array.shape[0] - 1):
		for j in range(1, image_array.shape[1] - 1):
			sub_matrix = image_array[i - 1:i + 1, j - 1:j + 1]
			gradient_x[i, j] = np.sum(sub_matrix * roberts_x)
			gradient_y[i, j] = np.sum(sub_matrix * roberts_y)

	# Compute the magnitude and direction of the gradient
	gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
	gradient_direction = np.arctan2(gradient_y, gradient_x)
	# Normalize the gradient magnitude values to the range [0, 255]
	min_val = np.min(gradient_magnitude)
	max_val = np.max(gradient_magnitude)
	gradient_magnitude = (gradient_magnitude - min_val) / (max_val - min_val) * 255

	# Convert the gradient values to 8-bit integers
	gradient_magnitude = np.uint8(gradient_magnitude)

	# Create an image from the gradient magnitude values
	gradient_image = Image.fromarray(gradient_magnitude)

	# Save the image to a file
	gradient_image.save('gradient_image.jpg')
	# Open the image
	image = Image.open('gradient_image.jpg')

	# Display the image
	image.show()
