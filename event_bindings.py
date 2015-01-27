from tkinter import *
from tkinter import ttk

root = Tk()

def key(event):
    print("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=True, height=True)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
ttk.Sizegrip().pack(side='right')
frame.pack()

root.mainloop()