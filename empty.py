#!/usr/bin/env python3
from tkinter import *

root = Tk()

blacke = Canvas(root, bg="black", width=400, height=200)
hello = Label(root, text="Hello")

#blacke.grid(columnspan=3)
hello.pack()

#hello.pack()
root.mainloop() 
locals