from tkinter import  *
from random import randint
from tkinter import messagebox
n = 'Тебе не повезет'
m = 'Тебе повезет'
def num_1():
    x = randint(1, 10)
    if x == '2':
        messagebox.showinfo('Результат', m)
    else:
        messagebox.showinfo('Результат', n)
root = Tk()
root.title('Приложение')
root.geometry("800x450")
root.resizable(False, False)
bnn = Button(root, text='Играть', width=10, height=2, bg='white', command=num_1)
bnn.pack()


root.mainloop()
