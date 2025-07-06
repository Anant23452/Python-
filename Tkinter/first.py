from tkinter import *

win = Tk()
win.title("My First Window")
win.geometry("300x200")

label = Label(win, text="Hello Annt! 👋", font=("Arial", 16))
label.pack(pady=20)

win.mainloop()
