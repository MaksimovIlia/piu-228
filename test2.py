from tkinter import *
import random


def raf_3():
    x =  int(random.randint(1, 3))
    if x == 1:
        num_1()
    elif x == 2:
        num_2()
    else:
        num_3()


def num_1():
    canvas = Canvas(root, width=200, height=200, bg='white')
    canvas.pack()
    canvas.create_rectangle(15, 15, 190, 110)


def num_2():
    canvas = Canvas(root, width=200, height=200, bg='white')
    canvas.pack()
    canvas.create_polygon(15, 15, 190, 110, 110, 50, fill='yellow', outline='black')


def num_3():
    canvas = Canvas(root, width=200, height=200, bg='white')
    canvas.pack()
    canvas.create_oval(15, 15, 190, 110)


root = Tk()
root.geometry("400x200")
root.resizable(False, False)
Button(root, text='Начать', width=10, height=2, bg='white', command=raf_3).pack()

root.mainloop()
