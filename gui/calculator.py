from tkinter import *
root = Tk()
root.title("simple Calculator")
root.geometry('400x300')
root.config(bg='#F2B33D')

frame = Frame(root, bg='#F2B33D')
e = Entry(root, width=45,  borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return None

def button_add():
    firstNum = e.get()
    global fNum
    fNum = int(firstNum)
    e.delete(0, END)
    global actionFlag
    actionFlag = 1

def button_sub():
    firstNum = e.get()
    global fNum
    fNum = int(firstNum)
    e.delete(0, END)
    global actionFlag
    actionFlag = 2

def button_mult():
    firstNum = e.get()
    global fNum
    fNum = int(firstNum)
    e.delete(0, END)
    global actionFlag
    actionFlag = 3

def button_div():
    firstNum = e.get()
    global fNum
    fNum = int(firstNum)
    e.delete(0, END)
    global actionFlag
    actionFlag = 4

def button_power():
    firstNum = e.get()
    global fNum
    fNum = int(firstNum)
    e.delete(0, END)
    global actionFlag
    actionFlag = 5

def button_equal():
    secondNum = e.get()
    e.delete(0, END)
    if actionFlag == 1:
        e.insert(0, fNum + int(secondNum))
    elif actionFlag == 2:
        e.insert(0, fNum - int(secondNum))
    elif actionFlag == 3:
        e.insert(0, fNum * int(secondNum))
    elif actionFlag == 4:
        e.insert(0, fNum / int(secondNum))
    elif actionFlag == 5:
        e.insert(0, fNum ** int(secondNum))

def button_clear():
    e.delete(0, END)
# define buttonsf

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=3,column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=3,column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=3,column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=2,column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=2,column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=2,column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=1,column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=1,column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=1,column=2)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0)).grid(row=4,column=0)
button_add = Button(root, text="+", padx=90, pady=20, command=button_add).grid(row=4, column=1, columnspan=2)
button_equal = Button(root, text="=", padx=40, pady=20, command= button_equal).grid(row=4, column=3)
button_clear = Button(root, text="clear", padx=34, pady=20, command=button_clear).grid(row=1, column=3)
button_sub = Button(root, text="-", padx=40, pady=4, command=None).grid(row=2, column=3, sticky=S)
button_mult = Button(root, text="x", padx=40, pady=4, command=None).grid(row=2, column=3, sticky=N)
button_div = Button(root, text="/", padx=40, pady=4, command=None).grid(row=3, column=3, sticky=N)
button_power = Button(root, text="^", padx=40, pady=4, command=None).grid(row=3, column=3, sticky=S)



root.mainloop()
