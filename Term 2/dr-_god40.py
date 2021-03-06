import tkinter as tk
import tkinter.ttk as ttk
import reg 


def callback(a ,b ,c):
    c = code.get()
    e4.config(bg="red")
    if c.isdigit():
        if len(c == 10:)
            e4.config(bg="green")
        elif len(c) > 10:
            code.set(c[:10])
            e4.config(bg="green")
    elif len(c) > 10:
        code.set(c[:10])





def register():
    reg.register(
        name.get(),
        last.get(),
        birth.get(),
        code.get(),
    )


root = tk.Tk()

name = tk.stringvar()
e1 = tk.Entry(root,textvariable=name)
e1.grid(row=0, column=1)

last = tk.stringvar()
e2 = tk.Entry(root,textvariable=last)
e2.grid(row=1, column=1)

birth = tk.stringvar()
e3 = tk.Entry(root,textvariable=last)
e3.grid(row=2, column=1)

code = tk.stringvar()
code.trace("w", callback)
e4 = tk.Entry(root, textvariable=code)
e4.grid(row=3, column=1)


fram = tk.Frame()
fram.grid(row=4, column=0, columnspan=2)

tk.Button(fram,text='register', command=register).grid(row=0, column=0)
tk.Button(fram,text='cancel', comman=root.destroy).grid(row=0, column=1)

root. mainloop()




