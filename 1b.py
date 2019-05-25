from tkinter import *

def inc():
    global n
    n.set(n.get() + 1)
    print("hello")

def dec():
    global n
    n.set(n.get() - 1)
    print("hello")

root = Tk()

n = IntVar()
root.title("updown")

Button(root, text = "UP", command = inc).pack()
Button(root, text = "DOWN", command = dec).pack()

l = Label(root, textvariable = n)
l.pack()

root.mainloop()
