




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







def Interpolation_Bilinear(filename):

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
			# Calculate the corresponding pixel in the input image using bilinear interpolation
			input_x = x / scaling_factor
			input_y = y / scaling_factor

			x1 = int(input_x)
			y1 = int(input_y)
			x2 = x1 + 1
			y2 = y1 + 1

			fx = input_x - x1
			fy = input_y - y1

			pixels = input_image[y1:y2 + 1, x1:x2 + 1]
			output_pixel = (1 - fx) * (1 - fy) * pixels[0, 0] + \
						   fx * (1 - fy) * pixels[0, 1] + \
						   (1 - fx) * fy * pixels[1, 0] + \
						   fx * fy * pixels[1, 1]

			# Set the value of the output pixel to the value calculated using bilinear interpolation
			output_image[y, x] = output_pixel

	# Save the output image
	cv2.imshow("Original", input_image)
	cv2.imshow("Resized", output_image)


