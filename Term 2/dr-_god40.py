import tkinter as tk

import reg 

def register():
    reg.register(
        name.get(),
        last.get(),
        birth.get(),
        code.get(),
    )


root = tk.Tk()

tk.Label(root,text='name').grid(row=0, column=0)
name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Label(root, text='last').grid(row=1, column=0)
last = tk.Entry(root)
last.grid(row=1, column=1)

tk.Label(root, text='birth date').grid(row=2, column=0)
birth = tk.Entry(root,  )
birth.grid(row=2, column=1)


tk.Label(root, text='id code').grid(row=3, column=0)
code = tk.Entry(root,  )
code.grid(row=3, column=1)


frame = tk.Frame(root)
frame.grid(row=6, column=0, columnspan=2)

tk.Button(frame,text='register', command=register).grid(row=0, column=0)
tk.Button(frame,text='cancel', comman=root.destroy).grid(row=0, column=1)

root. mainloop()




