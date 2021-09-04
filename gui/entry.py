from tkinter import *
root = Tk()
# to create text entry box
e  = Entry(root, width=50, bg="skyblue")
# to put instruction text inside text box
e.insert(0, "Enter your name")
e.pack()
def myClick():
    myLabel = Label(root, text="hello "+e.get())
    myLabel.pack()
# to create a button 
myButton = Button(root, text="click me", padx=10, pady=5, command=myClick, bg="#900000") #you can write the coulur name too
myButton.pack()
root.mainloop()
