from tkinter import *


class Gui:
    SIZE = 5
    EXPANDED = False

    def __init__(self, window):
        self.window = window

        self.entry_zone = Frame(self.window)
        self.main_entry = Entry(self.entry_zone, font=("Arial", 20), width= 4 * self.SIZE)
        self.button_enter = Button(self.entry_zone, text='=')
        self.main_entry.pack(anchor='w', side=LEFT)
        self.button_enter.pack(side=LEFT)
        self.entry_zone.pack(anchor='w', side=TOP)

        self.first_row = Frame(self.window)
        self.button_1 = Button(self.first_row, height=self.SIZE, width=2 * self.SIZE, text='1')
        self.button_2 = Button(self.first_row, height=self.SIZE, width=2 * self.SIZE, text='2')
        self.button_3 = Button(self.first_row, height=self.SIZE, width=2 * self.SIZE, text='3')
        self.button_add = Button(self.first_row, height=self.SIZE, width=2 * self.SIZE, text='+')
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')
        self.button_3.pack(side='left')
        self.button_add.pack(side='left')
        self.first_row.pack(anchor='w', side=TOP)

        self.second_row = Frame(self.window)
        self.button_4 = Button(self.second_row, height=self.SIZE, width=2 * self.SIZE, text='4')
        self.button_5 = Button(self.second_row, height=self.SIZE, width=2 * self.SIZE, text='5')
        self.button_6 = Button(self.second_row, height=self.SIZE, width=2 * self.SIZE, text='6')
        self.button_subtract = Button(self.second_row, height=self.SIZE, width=2 * self.SIZE, text='-')
        self.button_4.pack(side='left')
        self.button_5.pack(side='left')
        self.button_6.pack(side='left')
        self.button_subtract.pack(side='left')
        self.second_row.pack(anchor='w', side=TOP)

        self.third_row = Frame(self.window)
        self.button_7 = Button(self.third_row, height=self.SIZE, width=2 * self.SIZE, text='7')
        self.button_8 = Button(self.third_row, height=self.SIZE, width=2 * self.SIZE, text='8')
        self.button_9 = Button(self.third_row, height=self.SIZE, width=2 * self.SIZE, text='9')
        self.button_multiply = Button(self.third_row, height=self.SIZE, width=2 * self.SIZE, text='*')
        self.button_7.pack(side='left')
        self.button_8.pack(side='left')
        self.button_9.pack(side='left')
        self.button_multiply.pack(side='left')
        self.third_row.pack(anchor='w', side=TOP)

        self.fourth_row = Frame(self.window)
        self.button_clear = Button(self.fourth_row, height=self.SIZE, width=2 * self.SIZE, text='C')
        self.button_0 = Button(self.fourth_row, height=self.SIZE, width=2 * self.SIZE, text='0')
        self.button_advanced = Button(self.fourth_row, height=self.SIZE, width=2 * self.SIZE, text='Advanced', command=self.window_expand)
        self.button_divide = Button(self.fourth_row, height=self.SIZE, width=2 * self.SIZE, text='/')
        self.button_clear.pack(side='left')
        self.button_0.pack(side='left')
        self.button_advanced.pack(side='left')
        self.button_divide.pack(side='left')
        self.fourth_row.pack(anchor='w', side=TOP)


    def window_expand(self):
        if not self.EXPANDED:
            self.window.geometry("750x400")
            self.EXPANDED = True
        else:
            self.window.geometry("350x400")
            self.EXPANDED = False