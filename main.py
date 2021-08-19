#!/usr/local/bin/python
from tkinter import *
import os

window = Tk()
window.title("Password Generator")
window.geometry('550x200')


def run():
  os.system('python3 Generator.py')

btn = Button(window, text="Click Me", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)

window.mainloop()



