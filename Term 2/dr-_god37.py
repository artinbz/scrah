import tkinter as tk

root = tk.Tk()

l1 = tk.Label(root, text='L1', font=('times', 20),width=5)
l1.grid(row=0, column=0)
l2 = tk.Label(root, text='L2', font=('times', 20),width=5)
l2.grid(row=0, column=1)
l3 = tk.Label(root, text='L3', font=('times', 20),width=5)
l3.grid(row=1, column=0)
l4 = tk.Label(root, text='L3', font=('times', 20),width=5)
l4.grid(row=1, column=1)
l5 = tk.Label(root, text='L4', font=('times', 20),width=5)
l5.grid(row=3, column=1)
l6 = tk.Label(root, text='L5', font=('times', 20),width=5)
l6.grid(row=3, column=1)
root.mainloop()



