from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import cv2

root = Tk()
root.title('8-Bit Solver ')
# open dialogue box to browse file
filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select A File",
                                      filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
# show the choosen file
Opened_Img = ImageTk.PhotoImage(Image.open(filename))
myimg = Label(image=Opened_Img).pack()




# bit-1 function
def Bit1(filename):
    img = cv2.imread(filename, 0)
    image_One = (np.array([int(i[7]) for i in Pixels], dtype=np.uint8) * 1).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_One)
    cv2.waitKey(0)


# bit-1 button
Button_Bit1 = Button(root, text='1-Bit', padx=10, pady=10, command=lambda: Bit1(str(filename)))

# bit-2 button
Button_Bit2 = Button(root, text='2-Bit', padx=10, pady=10, command=lambda: Bit2(str(filename)))


# bit-2 function
def Bit2(filename):
    img = cv2.imread(filename, 0)
    image_Two = (np.array([int(i[6]) for i in Pixels], dtype=np.uint8) * 2).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Two)
    cv2.waitKey(0)




# bit-3 function
def Bit3(filename):
    img = cv2.imread(filename, 0)
    image_Three = (np.array([int(i[5]) for i in Pixels], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Three)
    cv2.waitKey(0)


# bit-3 button
Button_Bit3 = Button(root, text='3-Bit', padx=10, pady=10, command=lambda: Bit3(str(filename)))

# bit-4 function
def Bit4(filename):
    img = cv2.imread(filename, 0)
    image_Four = (np.array([int(i[4]) for i in Pixels], dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Four)
    cv2.waitKey(0)


# bit-4 button
Button_Bit4 = Button(root, text='4-Bit', padx=10, pady=10, command=lambda: Bit4(str(filename)))

# bit-5 function
def Bit5(filename):
    img = cv2.imread(filename, 0)
    image_Five = (np.array([int(i[3]) for i in Pixels], dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Five)
    cv2.waitKey(0)


# bit-5 button
Button_Bit5 = Button(root, text='5-Bit', padx=10, pady=10, command=lambda: Bit5(str(filename)))


# bit-6 function
def Bit6(filename):
    img = cv2.imread(filename, 0)
    image_Six = (np.array([int(i[2]) for i in Pixels], dtype=np.uint8) * 32).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Six)
    cv2.waitKey(0)


# bit-6 button
Button_Bit6 = Button(root, text='6-Bit', padx=10, pady=10, command=lambda: Bit6(str(filename)))


# bit-7 function
def Bit7(filename):
    img = cv2.imread(filename, 0)
    image_Seven = (np.array([int(i[1]) for i in Pixels], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Seven)
    cv2.waitKey(0)


# bit-7 button
Button_Bit7 = Button(root, text='7-Bit', padx=10, pady=10, command=lambda: Bit6(str(filename)))


# bit-8 function
def Bit8(filename):
    img = cv2.imread(filename, 0)
    image_Eight = (np.array([int(i[0]) for i in Pixels], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])
    cv2.imshow('a', image_Eight)
    cv2.waitKey(0)


# bit-8 button
Button_Bit8 = Button(root, text='8-Bit', padx=10, pady=10, command=lambda: Bit8(str(filename)))



def ShowAll(filename):
    img = cv2.imread(filename, 0)
    image_One = (np.array([int(i[7]) for i in Pixels], dtype=np.uint8) * 1).reshape(img.shape[0], img.shape[1])
    image_Two = (np.array([int(i[6]) for i in Pixels], dtype=np.uint8) * 2).reshape(img.shape[0], img.shape[1])
    image_Three = (np.array([int(i[5]) for i in Pixels], dtype=np.uint8) * 4).reshape(img.shape[0], img.shape[1])
    image_Four = (np.array([int(i[4]) for i in Pixels], dtype=np.uint8) * 8).reshape(img.shape[0], img.shape[1])
    image_Five = (np.array([int(i[3]) for i in Pixels], dtype=np.uint8) * 16).reshape(img.shape[0], img.shape[1])
    image_Six = (np.array([int(i[2]) for i in Pixels], dtype=np.uint8) * 32).reshape(img.shape[0], img.shape[1])
    image_Seven = (np.array([int(i[1]) for i in Pixels], dtype=np.uint8) * 64).reshape(img.shape[0], img.shape[1])
    image_Eight = (np.array([int(i[0]) for i in Pixels], dtype=np.uint8) * 128).reshape(img.shape[0], img.shape[1])

    #Concatenate these images for ease of display using cv2.hconcat()
    finalr = cv2.hconcat([image_Eight,image_Seven,image_Six,image_Five])
    finalv =cv2.hconcat([image_Four,image_Three,image_Two,image_One])

    # Vertically concatenate
    final = cv2.vconcat([finalr,finalv])

    # Display the images
    cv2.imshow('a',final)
    cv2.waitKey(0)

    cv2.waitKey(0)


# bit-8 button
Button_All = Button(root, text='Show All', padx=10, pady=10, command=lambda: ShowAll(str(filename)))




def Mix1(filename):
    img = cv2.imread(filename, 0)
    image_Five = (np.array([int(i[3]) for i in Pixels]) * 16).reshape(img.shape[0], img.shape[1])
    image_Six = (np.array([int(i[2]) for i in Pixels]) * 32).reshape(img.shape[0], img.shape[1])
    image_Seven = (np.array([int(i[1]) for i in Pixels]) * 64).reshape(img.shape[0], img.shape[1])
    image_Eight = (np.array([int(i[0]) for i in Pixels]) * 128).reshape(img.shape[0], img.shape[1])
    # Combining 4 bit planes
    new_img = image_Eight + image_Seven + image_Six + image_Five
    # Display the image
    cv2.imshow('a', new_img)
    cv2.waitKey(0)




# Mix2 button
Button_Mix1 = Button(root, text='1+2+3+4', padx=10, pady=10, command=lambda: Bit8(str(filename)))


def Mix2(filename):
    img = cv2.imread(filename, 0)
    image_One = (np.array([int(i[7]) for i in Pixels]) * 1).reshape(img.shape[0], img.shape[1])
    image_Two = (np.array([int(i[6]) for i in Pixels]) * 2).reshape(img.shape[0], img.shape[1])
    image_Three = (np.array([int(i[5]) for i in Pixels]) * 4).reshape(img.shape[0], img.shape[1])
    image_Four = (np.array([int(i[4]) for i in Pixels]) * 8).reshape(img.shape[0], img.shape[1])
    # Combining 4 bit planes
    new_img2 = image_One+image_Two+image_Three+image_Four
    # Display the image
    cv2.imshow('a',new_img2)
    cv2.waitKey(0)




# Mix2 button
Button_Mix2 = Button(root, text='5+6+7+8', padx=10, pady=10, command=lambda: Bit8(str(filename)))



# Read the given image
img = cv2.imread(filename, 0)






# function return the binary value
def decimalToBinary(n, k=0):
    if (n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n // 2)

    var = n % 2


# print(var, end=' ')



#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
Pixels = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # lst.append(decimalToBinary(img[i][j]))
        Pixels.append(np.binary_repr(img[i][j], width=8))  # width = no. of bits






#calling buttons
Button_Bit1.pack(expand=True ,fill='both')
Button_Bit2.pack(expand=True,fill='both')
Button_Bit3.pack(expand=True,fill='both')
Button_Bit4.pack(expand=True,fill='both')
Button_Bit5.pack(expand=True,fill='both')
Button_Bit6.pack(expand=True,fill='both')
Button_Bit7.pack(expand=True,fill='both')
Button_Bit8.pack(expand=True,fill='both')
Button_All.pack(expand=True,fill='both')
Button_Mix1.pack(expand=True,fill='both')
Button_Mix2.pack(expand=True,fill='both')







# loops while u close ur dialogue box
root.mainloop()
