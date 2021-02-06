import tkinter as tk
from tkinter import font 

def add():
    number = int(e1.get()) + int(e2.get())
    l1.config(text=number)

dark = {
    'bg': '#000000',
    'fg': '#ffffff',
    'font': ('times',20)
}

root = tk.Tk()
root.config(bg='#000000')


l1 = tk.Label(root, text='')
l1.pack()

e1 = tk.Entry(root, cnf=dark)
e1.pack()
e2 = tk.Entry(root, cnf=dark)
e2.pack()

b1 = tk.Button(root, text='+', command=add)
b1.pack()
root.mainloop()
