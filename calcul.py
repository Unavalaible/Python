#!/usr/bin/env python3

from tkinter import *
root = Tk()
root.title("calcul")
root.geometry("400x200")

result = 0
def sum():
    nu1 = int(number1.get())
    nu2 = int(number2.get())
    result = nu1+nu2
    r.config(text = result)


number1 = Entry(root)
number1.pack()
plus_sign = Label(root,text="+")
plus_sign.pack()
number2 = Entry(root)
number2.pack()

Button(root,text="calcul",command=sum).pack()
r = Label(root,text = result)
r.pack()

root.mainloop()
