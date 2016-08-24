import tkinter
from tkinter import *



def resize(ev = None):
    label.config(font='Helvetica - %d bold' %\
                      scale.get())

top = tkinter.Tk()
label = tkinter.Label(top,text_='Hello World!', bg='red', font='Helvetica -12 bold')
label.pack()

scale = Scale(top, from_=10, to=30, orient=HORIZONTAL, command=resize())
scale.set(12)
scale.pack()

button =tkinter.Button(top, text='按钮', command=top.quit, background='green')
button.pack()

tkinter.mainloop()