from tkinter import *
import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv


#get some basic windows stuff in first
window = Tk()
window.title("OPR v DPR v CCWM")
window.geometry('800x600')

#Team Number Enter
def hi():
        print(startEntry.get())


window=tkinter.Tk()

startLabel =window.Label(window,text="Enter Star: ")
startEntry=window.Entry(window)


startLabel.pack()
startEntry.pack()

plotButton= window.Button(window,text="plot", command=hi)

plotButton.pack()


#Enter in the Year

variable = StringVar(window)
variable.set("2019") # default value
w = OptionMenu(window, variable, "2002", "2003", "2019")
w.pack()


#call a function after okay button
def ok():
    year = variable.get()
    print (year)


#ok button
button = Button(window, text="Year OK", command=ok)
button.pack()

window.mainloop()
