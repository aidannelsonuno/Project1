from tkinter import *


class Gui:
    SIZE = 5

    def __init__(self, window):
        self.window = window

        #self.main_entry = Entry(font=("Arial", 20), width= 4 * self.SIZE)
        #self.main_entry.grid(row=0, column=0)side=TOP)

        self.button_grid = Frame(self.window)
        self.button_1 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='1')
        self.button_2 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='2')
        self.button_3 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='3')
        self.button_add = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='+')
        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_add.grid(row=0, column=3)
        self.button_4 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='4')
        self.button_5 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='5')
        self.button_6 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='6')
        self.button_subtract = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='-')
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_subtract.grid(row=1, column=3)
        self.button_7 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='7')
        self.button_8 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='8')
        self.button_9 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='9')
        self.button_multiply = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='*')
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_multiply.grid(row=2, column=3)
        self.button_clear = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='C')
        self.button_0 = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='0')
        self.button_enter = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='=')
        self.button_divide = Button(self.button_grid, height=self.SIZE, width=self.SIZE, text='/')
        self.button_clear.grid(row=3, column=0)
        self.button_0.grid(row=3, column=1)
        self.button_enter.grid(row=3, column=2)
        self.button_divide.grid(row=3, column=3)


