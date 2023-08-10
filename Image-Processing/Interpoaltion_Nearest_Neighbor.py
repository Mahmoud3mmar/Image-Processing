







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





def Interpoaltion_Nearest_Neighbor(filename):
	# Load the input image
	input_image = cv2.imread(filename)

	# Get the dimensions of the input image
	input_height, input_width, _ = input_image.shape

	# Set the dimensions of the output image
	output_height = 200
	output_width = 200

	# Calculate the scaling factor for the interpolation
	scaling_factor = min(output_width / input_width, output_height / input_height)

	# Create an empty output image
	output_image = np.zeros((output_height, output_width, 3), dtype=np.uint8)

	# Iterate over the pixels in the output image
	for y in range(output_height):
		for x in range(output_width):
			# Calculate the corresponding pixel in the input image
			input_x = int(round(x / scaling_factor))
			input_y = int(round(y / scaling_factor))

			# Set the value of the output pixel to the value of the corresponding input pixel
			output_image[x, y] = input_image[input_x, input_y]

	# Save the output image

	cv2.imshow("Original", input_image)
	cv2.imshow("Resized", output_image)
