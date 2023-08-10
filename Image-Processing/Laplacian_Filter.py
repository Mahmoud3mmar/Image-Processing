
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









def Laplacian_Filter(filename):
	def convolve2D(image, kernel, padding=0, strides=1):
		# Cross Correlation
		kernel = np.flipud(np.fliplr(kernel))

		# Gather Shapes of Kernel + Image + Padding
		xKernShape = kernel.shape[0]
		yKernShape = kernel.shape[1]
		xImgShape = image.shape[0]
		yImgShape = image.shape[1]

		# Shape of Output Convolution
		xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 3)
		yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 3)
		output = np.zeros((xOutput, yOutput))

		# Apply Equal Padding to All Sides
		if padding != 0:
			imagePadded = np.zeros((image.shape[0] + padding * 2, image.shape[1] + padding * 2))
			imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
			print(imagePadded)
		else:
			imagePadded = image

		# Iterate through image
		for y in range(image.shape[1]):
			# Exit Convolution
			if y > image.shape[1] - yKernShape:
				break
			# Only Convolve if y has gone down by the specified Strides
			if y % strides == 0:
				for x in range(image.shape[0]):
					# Go to next row once kernel is out of bounds
					if x > image.shape[0] - xKernShape:
						break
					try:
						# Only Convolve if x has moved by the specified Strides
						if x % strides == 0:
							output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
					except:
						break

		return output

	img = cv2.imread(filename, 0)

	plt.figure(figsize=(8, 5), dpi=150)
	plt.imshow(img, cmap='gray')
	plt.axis('off')
	plt.show()

	# kernel 1
	kernel = np.array([[0, 1, 0],
					   [1, -4, 1],
					   [0, 1, 0]])

	LaplacianImage = convolve2D(img,

								kernel=kernel)

	plt.figure(figsize=(8, 5), dpi=150)
	plt.imshow(LaplacianImage, cmap='gray')
	plt.axis('off')
	plt.show()

	c = -1
	g = img + c * LaplacianImage

	plt.figure(figsize=(8, 5), dpi=150)
	plt.imshow(g, cmap='gray')
	plt.axis('off')
	plt.show()

	gClip = np.clip(g, 0, 255)
	plt.figure(figsize=(8, 5), dpi=150)
	plt.imshow(gClip, cmap='gray')
	plt.axis('off')
	plt.show()


