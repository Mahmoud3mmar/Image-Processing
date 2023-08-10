
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












def Uniform_Noise(filename):
	import cv2
	import numpy as np

	# Load the image using OpenCV
	image = cv2.imread(filename)

	# Convert the image to grayscale
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Add uniform noise to the image
	def add_uniform_noise(image, min_val, max_val):
		# Generate an array of random noise values with the same shape as the image
		noise = np.random.uniform(min_val, max_val, image.shape)

		# Add the noise to the image
		noisy_image = image + noise

		# Clip the values of the noisy image to the range [0, 255]
		for i in range(noisy_image.shape[0]):
			for j in range(noisy_image.shape[1]):
				if noisy_image[i, j] < 0:
					noisy_image[i, j] = 0
				elif noisy_image[i, j] > 255:
					noisy_image[i, j] = 255

		return noisy_image.astype(np.uint8)

	# Call the add_uniform_noise() function with a minimum noise value of -50 and a maximum noise value of 50
	noisy_image = add_uniform_noise(gray_image, -50, 50)

	# Display the original and noisy images
	#cv2.imshow("Original", gray_image)
	cv2.imshow("Noisy", noisy_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

