import webbrowser
from tkinter import *
from tkinter import ttk

def launch():
    webbrowser.open_new('https://dropbox.com')

root = Tk()
root.title("Droppy")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Button(mainframe, text="Dropbox.com", command=launch).grid(column=0, row=0)

if __name__ == '__main__':
    root.mainloop()