from tkinter import *

def myClick():
    myLabel = Label(root, text="look I clicked")
    myLabel.pack()

root = Tk()
myButton = Button(root, text="click me", padx=10, pady=5, command=myClick, bg="#900000")
myButton.pack()
root.mainloop()
