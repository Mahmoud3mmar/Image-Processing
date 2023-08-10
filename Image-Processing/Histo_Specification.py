

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








def Histo_Specification(filename):
	import cv2

	def find_nearest_above(my_array, target):
		diff = my_array - target
		mask = np.ma.less_equal(diff, -1)
		# We need to mask the negative differences
		# since we are looking for values above
		if np.all(mask):
			c = np.abs(diff).argmin()
			return c # returns min index of the nearest if target is greater than any value
		masked_diff = np.ma.masked_array(diff, mask)
		return masked_diff.argmin()


	def hist_match(original, specified):

		oldshape = original.shape
		original = np.ravel(original)
		specified =np.ravel(specified)

		# get the set of unique pixel values and their corresponding indices and counts
		s_values, bin_idx, s_counts = np.unique(original, return_inverse=True,return_counts=True)
		t_values, t_counts = np.unique(specified, return_counts=True)

		# Calculate s_k for original image
		s_quantiles = np.cumsum(s_counts).astype(np.float64)
		s_quantiles /= s_quantiles[-1]

		# Calculate s_k for specified image
		t_quantiles = np.cumsum(t_counts).astype(np.float64)
		t_quantiles /= t_quantiles[-1]

		# Round the values
		sour = np.around(s_quantiles*255)
		temp = np.around(t_quantiles*255)

		# Map the rounded values
		b=[]
		for data in sour[:]:
			b.append(find_nearest_above(temp,data))
		b= np.array(b,dtype='uint8')

		return b[bin_idx].reshape(oldshape)

	import cv2
	import numpy as np

	# Load the images in greyscale
	original = cv2.imread(filename, 0)
	filename2 = filedialog.askopenfilename(initialdir="/Downloads", title="Select A File",
										  filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
	specified = cv2.imread(filename2, 0)

	# perform Histogram Matching
	a = hist_match(original, specified)

	# Display the image
	cv2.imshow('a2', specified)
	cv2.imshow('a', np.array(a, dtype='uint8'))
	cv2.imshow('a1', original)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# cv2_imshow(specified)
	# cv2_imshow(original)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	# Load the image
	image = cv2.imread('lena.png', 0)

	# Calculate histogram using cv2.calcHist()
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	# Display the histogram
	plt.plot(hist)

	plt.hist(image.flatten(), 256, [0, 256])
	plt.show()
