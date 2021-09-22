from tkinter import *

def myClick():
    myLabel = Label(root, text="look I clicked")
    myLabel.pack()

root = Tk()
myButton = Button(root, text="click me", padx=10, pady=5, command=myClick, bg="#900000") #you can write the coulur name too
myButton.pack()
root.mainloop()
