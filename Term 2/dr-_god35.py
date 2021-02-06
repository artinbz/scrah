import tkinter as tk 
from tkinter import Spinbox, font




root = tk.Tk()

spin = tk.Spinbox(root, from =0, to=9, wrap=True )
spin.pack()
root.mainloop()


