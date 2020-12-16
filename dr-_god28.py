import turtle as tr

def square(size):
    for i in range(4):
        tr.forward(size)
        tr.lt(90)

s = float(input('size of square: '))
square(s)
tr.done()