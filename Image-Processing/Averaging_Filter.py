




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



def Averaging_filter(filename):
	# Low Pass SPatial Domain Filtering
	# to observe the blurring effect
	# Averaging Filter:

	# Read the image
	img = cv2.imread(filename, 0)

	# Obtain number of rows and columns
	# of the image
	m, n = img.shape

	# Develop Averaging filter(3, 3) mask
	mask = np.ones([3, 3], dtype=int)
	mask = mask / 9

	# Convolve the 3X3 mask over the image
	img_new = np.zeros([m, n])

	for i in range(1, m - 1):
		for j in range(1, n - 1):
			temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
				i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
					   2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]

			img_new[i, j] = temp

	img_new = img_new.astype(np.uint8)
	cv2.imwrite('AverageFilter.jpg', img_new)
	cv2.imshow('AverageFilter', img_new)
	cv2.waitKey(0)
