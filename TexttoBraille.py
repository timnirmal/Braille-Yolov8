# create a gui to select the image and the output file

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Menu
import cv2

import os
import sys
import time
import cv2
import numpy as np
import json
import argparse
import shutil
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

from lib import predict


openFilePath = r"C:\Users\timni\PycharmProjects\Yolo\datasets\train\images"


# create gui

window = tk.Tk()
window.title("Text to Braille")
window.geometry("1020x540")

# # create frame
# frame = tk.Frame(window)
# frame.grid()
#
# # create a label as title in center
# lbl = tk.Label(window, text="Text to Braille", font=("Arial Bold", 50))
# lbl.grid()

def pickImage():
    file = filedialog.askopenfilename(initialdir=openFilePath, title='Select File',
                                      filetypes=(('JPG', '*.jpg'), ('All Files', '*.*')))
    print(file)

    # show the image in the gui
    image1 = Image.open(file)
    img = ImageTk.PhotoImage(image1)
    # panel = tk.Label(window, image=img)
    # panel.grid(column=0, row=0)

    # img = PhotoImage(file='image 2.png')
    # label = Label(window, image=img, width=34, height=48, bg='white')
    label = Label(window, image=img, bg='red')
    # resize image to fit label size
    label.image = img
    label.place(x=84, y=30)

    # predict the image
    result = predict.predict(file)

    fl = open(r"C:\Users\timni\PycharmProjects\Yolo\runs\detect\predict17\labels\0_2_jpg.rf.76b9c6cba32571b357830b5f3e74db1a.txt", 'r')
    data = fl.readlines()
    fl.close()

    img = cv2.imread(file)
    dh, dw, _ = img.shape

    print("data")
    print(data)
    print()

    print("dw")
    print(dw)
    print()

    print("dh")
    print(dh)
    print()

    print("img.shape")
    print(img.shape)
    print()


    for dt in data:

        # Split string to float
        _, x, y, w, h = map(float, dt.split(' '))

        print("x")
        print(x)
        print()

        print("y")
        print(y)
        print()

        print("w")
        print(w)
        print()

        print("h")
        print(h)
        print()

        # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
        # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)

        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1

        cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)

    plt.imshow(img)
    plt.show()

    # show the image in the gui
    image1 = Image.fromarray(img)
    img = ImageTk.PhotoImage(image1)
    # panel = tk.Label(window, image=img)
    # panel.grid(column=0, row=0)

    # img = PhotoImage(file='image 2.png')
    # label = Label(window, image=img, width=34, height=48, bg='white')
    label = Label(window, image=img, bg='red')
    # resize image to fit label size
    label.image = img
    label.place(x=84, y=30)


    # # show the result in the gui
    # txt = scrolledtext.ScrolledText(window, width=40, height=10)
    # txt.grid(column=0, row=1)
    # txt.insert(INSERT, result)
    # txt.configure(state='disabled')


    # create 3x2 grid of colored circles
    for row in range(3):
        for col in range(2):
            color = "red" if row % 2 == col % 2 else "black"
            tk.Label(window, text=".", bg=color, width=2, height=1).grid(row=row, column=col)













# create a button below the label
btn = tk.Button(window, text="Click Me", command=pickImage)
btn.grid(column=0, row=1)






#
# # create a label as title in center
# lbl = tk.Label(window, text="Text to Braille", font=("Arial Bold", 50))
# lbl.grid()
#
#
# def clicked():
#     lbl.configure(text="Button was clicked !!")
#
# # create a button below the label
# btn = tk.Button(window, text="Click Me", command=clicked)
# btn.grid(column=0, row=1)
#
# # create a text box
# txt = tk.Entry(window,width=100)
# txt.grid(column=0, row=2)
# txt.focus()
#
# # create box to show image test1.jpg
# image1 = Image.open("test.jpg")
# img = ImageTk.PhotoImage(image1)
# panel = tk.Label(window, image = img)
# panel.grid(column=0, row=3)
#
#
#
#
#
#
#
#
#
#




# start the gui
window.mainloop()


