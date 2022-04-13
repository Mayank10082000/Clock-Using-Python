#imported Tkinter for making GUI
from tkinter import *
from tkinter.ttk import *

'''strftime means string from time. 
we can format the time in different desirable ways.'''
from time import strftime

'''tk() displays root window and manages other components
of tkinter app'''
root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("Square Sans Serif 7", 200), background="black", foreground="red")
label.pack(anchor='center')
time()

mainloop()