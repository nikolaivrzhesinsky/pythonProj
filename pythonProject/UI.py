import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import cv2
import numpy
import os


def delete_files():
    files = os.scandir(putfolder_input.get())
    for file in files:
        os.remove(file)


def face_recognition(image, i):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
    faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    if len(faces_rect) > 0:
        cv2.imwrite(f'{putfolder_input.get()}/DetectedFace{i}.png', img)


def find_images_in_dict():
    delete_files()
    files = os.listdir(extraction_input.get())
    i = 0
    for file in files:
        face_recognition(os.path.join(extraction_input.get(), file), i)
        i += 1

window = Tk()
window.title('Face recognizing app')
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)
extraction_lb = Label(
    frame,
    text="Choose extraction folder"
)
extraction_lb.grid(row=1, column=1)

put_lb = Label(
    frame,
    text="Choose put folder"
)
put_lb.grid(row=2, column=1)

extraction_input = Entry(
    frame,
)
extraction_input.grid(row=1, column=2, pady=5)

putfolder_input = Entry(
    frame
)
putfolder_input.grid(row=2, column=2, pady=5)

recognizing_btn = Button(
    frame,
    text="Find pictures",
    command=find_images_in_dict
)
recognizing_btn.grid(row=3, column=2)


def open_extraction_file():
    extraction_input.insert(0, askdirectory())

def open_input_file():
    putfolder_input.insert(0, askdirectory())

open_extraction_folder_btn = Button(
    frame,
    text="choose",
    command=open_extraction_file
)
open_extraction_folder_btn.grid(row=1, column=3)

open_input_folder_btn = Button(
    frame,
    text="choose",
    command=open_input_file
)
open_input_folder_btn.grid(row=2, column=3)

window.mainloop()
