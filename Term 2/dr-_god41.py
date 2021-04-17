import tkinter as tk
from tkinter.constants import W
import tkinter.ttk as ttk
from typing import Text
import reg
from tkcalendar import DateEntry


def alphabet(a ,b ,c):
    if name.get().isalpha():
        e1.config(bg="green")
    else: 
        e1.config(bg="red")
        
def alphabet(a ,b ,c):
    if name.get().isalpha():
        e2.config(bg="green")
    else: 
        e2.config(bg="red")


def callback(a ,b ,c):
    c = code.get()
    e4.config(bg="red")
    if c.isdigit():
        if len(c) == 10:
            e4.config(bg='green')
        elif len(c) > 10:
            code.set(c[:10])
            e4.config(bg="green")
    elif len(c) > 10:
        code.set(v[:10])




def srch():
    file = open('name.txt', 'r')
    top = tk.Toplevel()
    top.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
    text = tk.Toplevel()
    text.grid(row=0, column=0)



def register():
    reg.register(
        name.get(),
        last.get(),
        birth.get(),
        code.get(),
    )

    name.set('')
    last.set('')
    code.set('')






root = tk.Tk()


tk.Label(root, text='name').grid(row=0, column=0)
tk.Label(root, text='Last Name').grid(row=1, column=0)
tk.Label(root, text='Birth Date').grid(row=2, column=0)
tk.Label(root, text='ID code').grid(row=3, column=0)

name = tk.StringVar()
name.trace("w", alphabet)
e1 = tk.Entry(root, textvariable=name)
e1.grid(row=0, column=1)

last = tk.StringVar()
last.trace("w", alphabet)
e2 = tk.Entry(root, textvariable=name)
e2.grid(row=1, column=1)

birth = tk.StringVar()
e3 = DateEntry(root, width=12, background='darkblue', foreground='white',
    borderwidth=2, deta_pettarn='y-mm-dd')
e3.grid(row=2, column1,)

code = tk.StringVar()
code.trace("w", alphabet)
e4 = tk.Entry(root, textvariable=name)
e4.grid(row=3, column=1)


frame = tk.Frame(root)
frame.grid(row=4, column=0, columnspan=2)

tk.Button(frame, text='register', command=register).grid(row=0, column=0)
tk.Button(frame, text='cancel', command=root.destroy).grid(row=0, column=1)

ttk.Separator(root,orient=tk.HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky="ew")

tk.Label(root, text='sratch').grid(row=6, column=0)
search = tk.Entry(root)
search.grid(row=6, column=1)
tk.Button(root, text='Search', command=srch).grid(row=7, column=0, columnspan=2)

root.mainloop()
