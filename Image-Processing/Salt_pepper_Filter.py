
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


def SaltAndPepper_Filter(filename):
	def add_noise(img):

		# Getting the dimensions of the image
		row, col = img.shape

		# Randomly pick some pixels in the
		# image for coloring them white
		# Pick a random number between 300 and 10000
		number_of_pixels = random.randint(300, 10000)
		for i in range(number_of_pixels):
			# Pick a random y coordinate
			y_coord = random.randint(0, row - 1)

			# Pick a random x coordinate
			x_coord = random.randint(0, col - 1)

			# Color that pixel to white
			img[y_coord][x_coord] = 255

		# Randomly pick some pixels in
		# the image for coloring them black
		# Pick a random number between 300 and 10000
		number_of_pixels = random.randint(300, 10000)
		for i in range(number_of_pixels):
			# Pick a random y coordinate
			y_coord = random.randint(0, row - 1)

			# Pick a random x coordinate
			x_coord = random.randint(0, col - 1)

			# Color that pixel to black
			img[y_coord][x_coord] = 0

		return img

	# salt-and-pepper noise can
	# be applied only to grayscale images
	# Reading the color image in grayscale image
	img = cv2.imread(filename,
					 cv2.IMREAD_GRAYSCALE)

	# Storing the image
	cv2.imwrite('salt-and-pepper-lena.jpg',
				add_noise(img))

	cv2.imshow('Salt&Pepper', img)
	cv2.waitKey(0)

