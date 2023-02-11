import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

from lib import predict

openFilePath = r"C:\Users\timni\PycharmProjects\Yolo\datasets\train\images"


def pickImage():
    file = filedialog.askopenfilename(initialdir=openFilePath, title='Select File',
                                      filetypes=(('JPG', '*.jpg'), ('All Files', '*.*')))
    print(file)

    # show the image in the gui
    image1 = Image.open(file)
    img = ImageTk.PhotoImage(image1)
    label = Label(middle, image=img, bg='red')
    label.place(x=80, y=80)

    # predict the image
    result = predict.predict(file)

    fl = open(
        r"C:\Users\timni\PycharmProjects\Yolo\runs\detect\predict17\labels\0_2_jpg.rf.76b9c6cba32571b357830b5f3e74db1a.txt",
        'r')
    data = fl.readlines()
    fl.close()

    img = cv2.imread(file)
    dh, dw, _ = img.shape

    for dt in data:
        # Split string to float
        _, x, y, w, h = map(float, dt.split(' '))

        # Convert to pixel
        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)

        # Check boundary
        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1

        # Draw rectangle
        cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)

    # show the image in the gui
    image1 = Image.fromarray(img)
    img = ImageTk.PhotoImage(image1)
    label = Label(middle, image=img, bg='red')
    label.image = img
    label.place(x=80, y=80)


if __name__ == '__main__':
    # Create Object and setup root
    root = Tk()
    root.title("Text to Braille")

    # Create Frames
    top = Frame(root, width=1440, height=100, bg='white')
    top.pack(side=TOP)
    middle = Frame(root, width=1440, height=630, bg='white')
    middle.pack(side=TOP)


    # Create Widgets

    """Top Section"""
    """Top Section"""
    """Top Section"""

    # create a label as title in center
    lbl = tk.Label(top, text="Text to Braille", font=("Arial Bold", 40))
    lbl.grid()


    """Image Section"""
    """Image Section"""
    """Image Section"""

    # show the image in the gui
    placeHolderImageOpen = Image.open('test.jpg')
    placeHolderImage = ImageTk.PhotoImage(placeHolderImageOpen)
    label = Label(middle, image=placeHolderImage, bg='red', width=416, height=416)
    label.place(x=80, y=80)

    # Button below the image to pick image and command= pickImage
    btn = tk.Button(middle, text="Pick Image", font=('arial', 15), width=10, height=1, bg='green', fg='white',command=pickImage)
    btn.place(x=200, y=530)


    root.mainloop()
