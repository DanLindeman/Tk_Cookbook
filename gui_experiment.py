from tkinter import *
from tkinter import ttk

def remove(*args):
    """Removes the last item from the listbox"""
    l.delete(l.size()-1)# Really wish l.delete(-1) worked instead...

def quit():
    """A callback to make Ctrl-C work"""
    root.quit()

    
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
lb_list = StringVar(value=(1,2,3,4,5,6,7,8))
ttk.Button(mainframe, text="Remove", command=remove).grid(column=0, row=0, sticky=W)
l = Listbox(mainframe, listvariable=lb_list, height=5)
l.grid(column=0, row=1, sticky=(N,W,E,S))
s = ttk.Scrollbar(mainframe, orient=VERTICAL, command=l.yview)
l.configure(yscrollcommand=s.set)
s.grid(column=0, row=1, sticky=(N,E,S))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
#root.bind('<Return>', calculate)
root.bind('<Delete>', remove)
root.bind('<Escape>', quit)

if __name__ == '__main__':
    root.mainloop()