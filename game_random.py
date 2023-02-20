from tkinter import  *
from numpy import *
from random import randint
from tkinter import messagebox
def num_1():
    x = randint(1,20)
    if x == '3':
        messagebox.showinfo('Сегодня, тебе повезет')
    else:
        messagebox.showinfo('Сегодня, тебе не повезет')
root = Tk()
root.title('Приложение')
root.geometry("800x450")
root.resizable(False, False)
bnn = Button(root, text='Играть', width=10, height=2, bg='white', command=num_1)
bnn.pack()


root.mainloop()