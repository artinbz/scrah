import tkinter as tk 




root = tk.Tk()

l1 = tk.Label(root, text='weight')
l1.grid(row=0, column=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)


l2 = tk.Label(root, text='height')
l2.grid(row=1, column=0)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)


frame  = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2)
l2 = tk.Label(frame, text='BMI')
l2.grid(row=1, column=0)
l2 = tk.Entry(frame,  )
l2.grid(row=2, column=1)
root.mainloop


root. mainloop()