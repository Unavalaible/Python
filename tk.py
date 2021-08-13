import tkinter
from typing import Text

mainapp = tkinter.Tk()
mainapp.title("lol")

def hello():
    print("Hello")


#windows size
screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()
window_x = 800
window_y = 600
decalage_x = int((screen_x//2) - (window_x//2))
decalage_y = int((screen_y//2) - (window_y//2))
geo = "{}x{}+{}+{}".format(window_x,window_y,decalage_x,decalage_y)
#mainapp.resizable(width=False,height=False)
mainapp.geometry(geo)

#labels
label_welcome = tkinter.Label(mainapp,text="Welcome")
label_welcome.config(text="mar7ba")

#entries
Entry_name = tkinter.Entry(mainapp)

#button
bottona = tkinter.Button(mainapp,text = "Hello", command=hello)

bottona.pack()
mainapp.mainloop()
