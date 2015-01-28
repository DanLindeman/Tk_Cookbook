#!usr/bin/env python
import os
from tkinter import *
from tkinter import ttk

def process_directory(parent, path):
    for p in os.listdir(path):
        abspath = os.path.join(path, p)
        isdir = os.path.isdir(abspath)
        oid = tree.insert(parent, 'end', text=p, open=False)
        if isdir:
            process_directory(oid, abspath)

root = Tk()
tree = ttk.Treeview(root)
tree.column("#0",minwidth=0, stretch=NO)
abspath = os.path.abspath(os.getcwd())
root_node = tree.insert('', 'end', text=abspath, open=True)
process_directory(root_node, abspath)
ysb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
xsb = ttk.Scrollbar(root, orient='horizontal', command=tree.xview)
tree.configure(yscroll=ysb.set, xscroll=xsb.set)
tree.grid(row=0, column=0, sticky='nesw')
ysb.grid(row=0, column=1, sticky='ns')
xsb.grid(row=1, column=0, sticky='ew')
root.grid()
root.mainloop()
