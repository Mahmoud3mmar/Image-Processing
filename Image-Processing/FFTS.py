




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






def ffts():
	# Load the image and convert it to grayscale
	img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
	def fft(x):
		N = x.shape[0]
		if N <= 1:
			return x
		even = fft(x[0::2])
		odd = fft(x[1::2])
		T = np.exp(-2j * np.pi * np.arange(N) / N)
		return concatenate([even + T[:N // 2] * odd,
							   even + T[N // 2:] * odd])




	def concatenate(arrays):
		# Create an empty list that will hold the concatenated arrays
		concatenated = []

		# Iterate over the list of arrays and append them to the list
		for array in arrays:
			concatenated.append(array)

		# Flatten the list of arrays into a single 1D array
		concatenated = np.array(concatenated).flatten()

		# Determine the shape of the concatenated array
		shape = [len(arrays)] + list(arrays[0].shape)

	# Reshape the 1D array into a multi-dimensional array
		fft(img)
		# Convert the image to a numpy array
		img_array = np.array(img)

		# Apply the FFT to the image
		fft_result = fft(img_array)

		# Save or display the FFT result
		np.save('fft_result.npy', fft_result)
		from PIL import Image

		# ffts(img, 100)
		cv2.imshow('fft filter', fft_result)
		cv2.waitKey(0)


