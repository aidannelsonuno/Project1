from tkinter import *


class Gui:
    EXPANDED = False
    HEIGHT = 5
    WIDTH = 10

    def __init__(self, window):
        self.window = window

        self.entry_zone = Frame(self.window)
        self.main_entry = Entry(self.entry_zone, font=("Arial", 20), width=2*self.WIDTH)
        self.button_enter = Button(self.entry_zone, text='=')
        self.main_entry.pack(anchor='w', side=LEFT)
        self.button_enter.pack(side=LEFT)
        self.entry_zone.pack(anchor='w', side=TOP)
        self.main_entry.insert(0, '0')
        self.main_entry.config(state=DISABLED)

        self.first_row = Frame(self.window)
        self.button_1 = Button(self.first_row, height=self.HEIGHT, width=self.WIDTH, text='1', command=lambda: self.enter('1'))
        self.button_2 = Button(self.first_row, height=self.HEIGHT, width=self.WIDTH, text='2', command=lambda: self.enter('2'))
        self.button_3 = Button(self.first_row, height=self.HEIGHT, width=self.WIDTH, text='3', command=lambda: self.enter('3'))
        self.button_add = Button(self.first_row, height=self.HEIGHT, width=self.WIDTH, text='+', command=lambda: self.enter('+'))
        self.button_1.pack(side='left')
        self.button_2.pack(side='left')
        self.button_3.pack(side='left')
        self.button_add.pack(side='left')
        self.first_row.pack(anchor='w', side=TOP)

        self.second_row = Frame(self.window)
        self.button_4 = Button(self.second_row, height=self.HEIGHT, width=self.WIDTH, text='4', command=lambda: self.enter('4'))
        self.button_5 = Button(self.second_row, height=self.HEIGHT, width=self.WIDTH, text='5', command=lambda: self.enter('5'))
        self.button_6 = Button(self.second_row, height=self.HEIGHT, width=self.WIDTH, text='6', command=lambda: self.enter('6'))
        self.button_subtract = Button(self.second_row, height=self.HEIGHT, width=self.WIDTH, text='-', command=lambda: self.enter('-'))
        self.button_4.pack(side='left')
        self.button_5.pack(side='left')
        self.button_6.pack(side='left')
        self.button_subtract.pack(side='left')
        self.second_row.pack(anchor='w', side=TOP)

        self.third_row = Frame(self.window)
        self.button_7 = Button(self.third_row, height=self.HEIGHT, width=self.WIDTH, text='7', command=lambda: self.enter('7'))
        self.button_8 = Button(self.third_row, height=self.HEIGHT, width=self.WIDTH, text='8', command=lambda: self.enter('8'))
        self.button_9 = Button(self.third_row, height=self.HEIGHT, width=self.WIDTH, text='9', command=lambda: self.enter('9'))
        self.button_multiply = Button(self.third_row, height=self.HEIGHT, width=self.WIDTH, text='*', command=lambda: self.enter('*'))
        self.button_7.pack(side='left')
        self.button_8.pack(side='left')
        self.button_9.pack(side='left')
        self.button_multiply.pack(side='left')
        self.third_row.pack(anchor='w', side=TOP)

        self.fourth_row = Frame(self.window)
        self.button_advanced = Button(self.fourth_row, height=self.HEIGHT, width=self.WIDTH, text='Advanced', command=self.window_expand)
        self.button_0 = Button(self.fourth_row, height=self.HEIGHT, width=self.WIDTH, text='0', command=lambda: self.enter('0'))
        self.button_clear = Button(self.fourth_row, height=self.HEIGHT, width=self.WIDTH, text='C', command=self.clear)
        self.button_divide = Button(self.fourth_row, height=self.HEIGHT, width=self.WIDTH, text='/', command=lambda: self.enter('/'))
        self.button_advanced.pack(side='left')
        self.button_0.pack(side='left')
        self.button_clear.pack(side='left')
        self.button_divide.pack(side='left')
        self.fourth_row.pack(anchor='w', side=TOP)


    def window_expand(self):
        if not self.EXPANDED:
            self.window.geometry("750x400")
            self.button_advanced.config(text="Simple")
            self.EXPANDED = True
        else:
            self.window.geometry("350x400")
            self.button_advanced.config(text="Advanced")
            self.EXPANDED = False

    
    def clear(self):
        self.main_entry.config(state=NORMAL)
        self.main_entry.delete(0, END)
        self.main_entry.insert(0, '0')
        self.main_entry.config(state=DISABLED)

    def enter(self, text_in):
        
        operators =  ['+', '-', '*', '/']
        expression = self.main_entry.get()
        if text_in in operators:
            if expression[-1] in operators:
                if text_in == '-' and expression[-1] != '-':
                    expression += text_in
        else:        
            expression += text_in
        self.main_entry.config(state=NORMAL)
        self.main_entry.delete(0, END)
        self.main_entry.insert(0, expression)
        self.main_entry.config(state=DISABLED)


        
