from tkinter import *
jarvis = Tk()
jarvis.geometry("410x410")
jarvis.minsize(200, 200)
jarvis.maxsize(410, 410)
jarvis.title("JARVIS")
jarvisImage = PhotoImage(file="jarvisImg.png")
jarvisLable = Label(image=jarvisImage, borderwidth=3, relief=SUNKEN)
jarvisLable.pack()

jarvis.mainloop()