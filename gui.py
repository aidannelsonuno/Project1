from tkinter import *
import math


class Gui:
    EXPANDED = False
    HEIGHT = 5
    WIDTH = 10

    def __init__(self, window: Tk) -> None:
        '''
        Initializes the GUI for the calculator and all of its widgets and necessary variables
        :param window: A Tk object used to create the GUI
        '''
        self.window = window

        self.num_stored = ''
        self.num_in = '0'
        self.operator = ''
        self.new_number = False
        
        self.entry_zone = Frame(self.window)
        self.entry_zone.grid(row=0, column=0)
        self.main_entry = Entry(self.entry_zone, font=("Arial", 20), width=2*self.WIDTH)
        self.main_entry.grid(row=0, column=0)

        self.main_entry.insert(0, '0')
        self.main_entry.config(state=DISABLED)
        
        self.simple_grid = Frame(self.window)
        self.simple_grid.grid(row=1, column=0)
        self.button_enter = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='=', command=self.evaluate)
        self.button_1 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='1', command=lambda: self.enter('1'))
        self.button_2 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='2', command=lambda: self.enter('2'))
        self.button_3 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='3', command=lambda: self.enter('3'))
        self.button_add = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='+', command=lambda: self.operation('+'))
        self.button_enter.grid(row=0, column=0)
        self.button_1.grid(row=0, column=1)
        self.button_2.grid(row=0, column=2)
        self.button_3.grid(row=0, column=3)
        self.button_add.grid(row=0, column=4)
        self.button_ac = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='AC', command=self.all_clear)
        self.button_4 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='4', command=lambda: self.enter('4'))
        self.button_5 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='5', command=lambda: self.enter('5'))
        self.button_6 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='6', command=lambda: self.enter('6'))
        self.button_subtract = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='-', command=lambda: self.operation('-'))
        self.button_ac.grid(row=1, column=0)
        self.button_4.grid(row=1, column=1)
        self.button_5.grid(row=1, column=2)
        self.button_6.grid(row=1, column=3)
        self.button_subtract.grid(row=1, column=4)
        self.button_clear = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='C', command=self.clear)
        self.button_7 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='7', command=lambda: self.enter('7'))
        self.button_8 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='8', command=lambda: self.enter('8'))
        self.button_9 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='9', command=lambda: self.enter('9'))
        self.button_multiply = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='*', command=lambda: self.operation('*'))
        self.button_clear.grid(row=2, column=0)
        self.button_7.grid(row=2, column=1)
        self.button_8.grid(row=2, column=2)
        self.button_9.grid(row=2, column=3)
        self.button_multiply.grid(row=2, column=4)
        self.button_advanced = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='Advanced', command=self.window_expand)
        self.button_decimal = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='.', command=lambda: self.enter('.'))
        self.button_0 = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='0', command=lambda: self.enter('0'))
        self.button_sign = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='+/-', command=lambda: self.enter('sign'))
        self.button_divide = Button(self.simple_grid, height=self.HEIGHT, width=self.WIDTH, text='/', command=lambda: self.operation('/'))
        self.button_advanced.grid(row=3, column=0)
        self.button_decimal.grid(row=3, column=1)
        self.button_0.grid(row=3, column=2)
        self.button_sign.grid(row=3, column=3)
        self.button_divide.grid(row=3, column=4)

        self.advanced_grid = Frame(self.window)
        self.advanced_grid.grid(row=1, column=1)
        self.button_pow = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='^', command=lambda: self.operation('^'))
        self.button_square = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='x^2', command=lambda: self.single_op('2'))
        self.button_sin = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='sin', command=lambda: self.single_op('sin'))
        self.button_pow.grid(row=0, column=0)
        self.button_square.grid(row=0, column=1)
        self.button_sin.grid(row=0, column=2)
        self.button_sqrt = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='sqrt', command=lambda: self.single_op('sqrt'))
        self.button_inverse = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='x^-1', command=lambda: self.single_op('-1'))
        self.button_cos = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='cos', command=lambda: self.single_op('cos'))
        self.button_sqrt.grid(row=1, column=0)
        self.button_inverse.grid(row=1, column=1)
        self.button_cos.grid(row=1, column=2)
        self.button_cuberoot = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='cbrt', command=lambda: self.single_op('cbrt'))
        self.button_ln = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='ln', command=lambda: self.single_op('ln'))
        self.button_tan = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='tan', command=lambda: self.single_op('tan'))
        self.button_cuberoot.grid(row=2, column=0)
        self.button_ln.grid(row=2, column=1)
        self.button_tan.grid(row=2, column=2)
        self.button_mod = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='Modulus', command=lambda: self.operation('%'))
        self.button_log = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='log', command=lambda: self.single_op('log'))
        self.button_fact = Button(self.advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='!', command=lambda: self.single_op('!'))
        self.button_mod.grid(row=3, column=0)
        self.button_log.grid(row=3, column=1)
        self.button_fact.grid(row=3, column=2)

        self.advanced_grid.grid_forget()
   
    def all_clear(self) -> None:
        '''
        Clears the calculator's view screen as well as the stored numbers from previous entries
        '''
        self.clear()
        self.num_stored = ''

    def clear(self) -> None:
        '''
        Clears the calculator view screen and any numbers entered since the last operation
        '''
        self.num_in = '0'
        self.replace_main_entry()

    def enter(self, pressed: str) -> None:
        '''
        Handles button input for buttons that enter digits, decimal points or sign changes
        :param pressed: The pressed button on the calculator that corresponds with an entered character
        '''
        if self.new_number:
            self.num_stored = self.num_in
            self.num_in = '0'
            self.new_number = False
        if pressed.isdigit():
            self.num_in = self.num_in + pressed if self.num_in != '0' else pressed
        elif pressed == 'sign' and self.num_in != '0':
            self.num_in = '-' + self.num_in if self.num_in[0] != '-' else self.num_in[1:]
        elif pressed == '.':
            if '.' not in self.num_in:
                self.num_in += '.'
        self.replace_main_entry()


    def operation(self, pressed) -> None:
        '''
        Designates the operator to be used based on user input
        :param pressed: The user's chosen operation
        '''
        if self.num_stored != '':
            self.evaluate()
        if self.operator != pressed:
            self.operator = pressed
            self.new_number = True
        else:
            self.operator = ''
            self.new_number = False

    def single_op(self, pressed) -> None:
        '''
        Handles processing the math for operations on one number
        :param pressed: The user's chosen operation
        '''
        if self.num_stored != '':
            self.evaluate()
        result = float(self.num_in)
        try:
            if self.num_in == '':
                raise ValueError
            if pressed == '2':
                result = float(self.num_in) ** 2
            elif pressed == '-1':
                if -1E-10 < float(self.num_in) < 1E-10:
                    raise ZeroDivisionError
                else:
                    result = float(self.num_in) ** -1
            elif pressed == 'sqrt':
                if float(self.num_in) < 1E-10:
                    raise ValueError
                else:
                    result = math.sqrt(float(self.num_in))
            elif pressed == 'cbrt':
                result = math.cbrt(float(self.num_in))
            elif pressed == '!':
                result = math.factorial(int(self.num_in))
            elif pressed == 'ln':
                if float(self.num_in) < 1E-10:
                    raise ValueError
                else:
                    result = math.log(float(self.num_in))
            elif pressed == 'log':
                if float(self.num_in) < 1E-10:
                    raise ValueError
                else:
                    result = math.log10(float(self.num_in))
            elif pressed == 'sin':
                result = math.sin(float(self.num_in))
            elif pressed == 'cos':
                result = math.cos(float(self.num_in))
            elif pressed == 'tan':
                result = math.tan(float(self.num_in))
            self.num_in = f'{result:.10f}'.rstrip('0').rstrip('.')
            self.operator = ''
            self.replace_main_entry()
        except ZeroDivisionError:
            self.show_error()
        except ValueError:
            self.show_error()
        except OverflowError:
            self.show_error()

    def evaluate(self) -> None:
        '''
        Handles the math for operations on two numbers, used by the operation function and linked to the = button on the calculator
        '''
        result = float(self.num_in)
        try:
            if self.num_stored == '':
                raise ValueError
            if self.operator == '+':
                result = float(self.num_stored) + float(self.num_in)
            elif self.operator == '-':
                result = float(self.num_stored) - float(self.num_in)
            elif self.operator == '*':
                result = float(self.num_stored) * float(self.num_in)
            elif self.operator == '/':
                if -1E-10 < float(self.num_in) < 1E-10:
                    raise ZeroDivisionError
                else:
                    result = float(self.num_stored) / float(self.num_in)
            elif self.operator == '^':
                if -1E-10 < float(self.num_in) < 1E-10 and -1E-10 < float(self.num_stored) < 1E-10:
                    raise ZeroDivisionError
                else:
                    result = math.pow(float(self.num_stored), float(self.num_in))
            elif self.operator == '%':
                result = float(self.num_stored) % float(self.num_in)
            self.num_in = str(result)
            self.num_stored = ''
            self.operator = ''
            self.replace_main_entry()
        except ZeroDivisionError:
            self.show_error()
        except OverflowError:
            self.show_error
        except ValueError:
            self.operator = ''

    def show_error(self) -> None:
        '''
        Function for displaying errors to the calculator and continuing functionality afterwards
        '''
        self.num_in = '0'
        self.num_stored = ''
        self.main_entry.config(state=NORMAL)
        self.main_entry.delete(0, END)
        self.main_entry.insert(0, 'ERROR')
        self.main_entry.config(state=DISABLED)

    def replace_main_entry(self) -> None:
        '''
        Replaces the contents of the entry box in the calculator with updated values
        '''
        self.main_entry.config(state=NORMAL)
        self.main_entry.delete(0, END)
        if float(self.num_in) < 1E10:
            self.main_entry.insert(0, f'{float(self.num_in):.10f}'.rstrip('0').rstrip('.'))
        else:
            magnitude = math.floor(math.log10(float(self.num_in)))
            self.main_entry.insert(0, f'{float(self.num_in)/math.pow(10, magnitude):.10f}E{magnitude}')
        self.main_entry.config(state=DISABLED)


    def window_expand(self) -> None:
        '''
        Expands and contracts the calculator window depending on if the user wishes to use the simple or advanced version
        '''
        if not self.EXPANDED:
            self.window.geometry("700x400")
            self.button_advanced.config(text="Simple")
            self.EXPANDED = True
            self.advanced_grid.grid(row=1, column=1)
        else:
            self.advanced_grid.grid_forget()
            self.window.geometry("450x400")
            self.button_advanced.config(text="Advanced")
            self.EXPANDED = False
            
        
