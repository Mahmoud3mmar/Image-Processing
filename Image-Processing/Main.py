
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


root = Tk()
root.title('Image Processing ')




filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select A File",
                                      filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))










########################################For the Spatial Domain filters









#Adaptive_Filter.py

import Adaptive_Filter


#Averaging_filter
import Averaging_Filter



#Median_filter

import Median_Filter


#Gaussian_filter
import Gaussian_Filter


#################################################Sharpening Spatial filters


#Laplacian_Filter
import Laplacian_Filter



#UnsharpMasking_Filter
import UnsharpMasking_Filter



#Roberts
import Roberts

#Sobel_filter.py
import Sobel_Filter


#################################################Noise Filters



#Uniform_Noise
import Uniform_Noise

# Salt&Pepper_Filter
import Salt_pepper_Filter

#Gaussian_Noise
import Gaussian_Noise

#Histo_Equalization

import Histo_Equalization


#Histo_Specification
import Histo_Specification




#FFTS
import FFTS


#Interpoaltion_Nearest_Neighbor
import Interpoaltion_Nearest_Neighbor

#Interpolation_Bilinear
import Interpolation_Bilinear

##############################################################

Button_SaltAndPepper = Button(root, text='Salt&Pepper', padx=10, pady=10, command=lambda: Salt_pepper_Filter.SaltAndPepper_Filter(str(filename)))


Button_Adaptive = Button(root, text='Adaptive Filter', padx=10, pady=10, command=lambda: Adaptive_Filter.Adaptive(str(filename)))

Button_Averaging_filter = Button(root, text='Average Filter', padx=10, pady=10, command=lambda: Averaging_Filter.Averaging_Filter(str(filename)))
Button_Median_filter= Button(root, text='Median Filter', padx=10, pady=10, command=lambda: Median_Filter.Median_Filter(str(filename)))
Button__Gaussian_filter= Button(root, text='Gaussian Filter', padx=10, pady=10, command=lambda: Gaussian_Filter.Gaussian_Filter(str(filename)))


##############################################################

Button_Laplacian_filter= Button(root, text='Laplacian Filter', padx=10, pady=10, command=lambda: Laplacian_Filter.Laplacian_Filter(str(filename)))
Button_Unsharp_filter= Button(root, text='Unsharp Filter', padx=10, pady=10, command=lambda: UnsharpMasking_Filter.UnsharpMasking_Filter(str(filename)))
Button_Roberts_filter= Button(root, text='Roberts Filter', padx=10, pady=10, command=lambda: Roberts.Roberts(str(filename)))


Button_Sobel_filter= Button(root, text='Sobel Filter', padx=10, pady=10, command=lambda: Sobel_Filter.Sobel_Filter(str(filename)))



Button_Uniform_noise_filter= Button(root, text='Uniform Noise', padx=10, pady=10, command=lambda: Uniform_Noise.Uniform_Noise(str(filename)))
Button__Gaussian_noise_filter= Button(root, text='Gaussian Noise', padx=10, pady=10, command=lambda: Gaussian_Noise.Gaussian_Noise(str(filename)))




Button_Histo_egualization_filter= Button(root, text='Histo Equalization', padx=10, pady=10, command=lambda: Histo_Equalization.Histo_Equalization(str(filename)))

Button_Histo_specification_filter= Button(root, text='Histo Specification', padx=10, pady=10, command=lambda: Histo_Specification.Histo_Specification(str(filename)))

Button_fft_filter= Button(root, text='fft filter', padx=10, pady=10, command=lambda: FFTS.ffts())


Button_interpoaltion_Nearest_neighbor= Button(root, text='Interpoaltion Nearest_neighbor', padx=10, pady=10, command=lambda: Interpoaltion_Nearest_Neighbor.Interpoaltion_Nearest_Neighbor(str(filename)))
Button_Interpolation_Bilinear= Button(root, text='Interpoaltion Bilinear', padx=10, pady=10, command=lambda: Interpolation_Bilinear.Interpolation_Bilinear(str(filename)))

Button_SaltAndPepper.pack(expand=True)
Button_Adaptive.pack(expand=True )

Button_Averaging_filter.pack(expand=True )
Button_Median_filter.pack(expand=True )
Button__Gaussian_filter.pack(expand=True)

Button_Laplacian_filter.pack(expand=True )
Button_Unsharp_filter.pack(expand=True )
Button_Roberts_filter.pack(expand=True )

Button_Sobel_filter.pack(expand=True )


Button_Uniform_noise_filter.pack(expand=True )
Button__Gaussian_noise_filter.pack(expand=True )

Button_Histo_egualization_filter.pack(expand=True )
Button_Histo_specification_filter.pack(expand=True )

Button_fft_filter.pack(expand=True )

Button_interpoaltion_Nearest_neighbor.pack(expand=True)
Button_Interpolation_Bilinear.pack(expand=True )






root.mainloop()

