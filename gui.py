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
        self.__window = window

        self.__num_stored = ''
        self.__num_shown = '0'
        self.__operator = ''
        self.__is_new_number = False
        
        self.__entry_zone = Frame(self.__window)
        self.__entry_zone.grid(row=0, column=0)
        self.__main_entry = Entry(self.__entry_zone, font=("Arial", 20), width=26)
        self.__main_entry.grid(row=0, column=0)

        self.__main_entry.insert(0, '0')
        self.__main_entry.config(state=DISABLED)
        
        self.__simple_grid = Frame(self.__window)
        self.__simple_grid.grid(row=1, column=0)
        self.__button_enter = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='=', command=self.__evaluate)
        self.__button_1 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='1', command=lambda: self.__enter('1'))
        self.__button_2 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='2', command=lambda: self.__enter('2'))
        self.__button_3 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='3', command=lambda: self.__enter('3'))
        self.__button_add = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='+', command=lambda: self.__operation('+'))
        self.__button_enter.grid(row=0, column=0)
        self.__button_1.grid(row=0, column=1)
        self.__button_2.grid(row=0, column=2)
        self.__button_3.grid(row=0, column=3)
        self.__button_add.grid(row=0, column=4)
        self.__button_ac = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='AC', command=self.__all_clear)
        self.__button_4 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='4', command=lambda: self.__enter('4'))
        self.__button_5 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='5', command=lambda: self.__enter('5'))
        self.__button_6 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='6', command=lambda: self.__enter('6'))
        self.__button_subtract = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='-', command=lambda: self.__operation('-'))
        self.__button_ac.grid(row=1, column=0)
        self.__button_4.grid(row=1, column=1)
        self.__button_5.grid(row=1, column=2)
        self.__button_6.grid(row=1, column=3)
        self.__button_subtract.grid(row=1, column=4)
        self.__button_clear = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='C', command=self.__clear)
        self.__button_7 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='7', command=lambda: self.__enter('7'))
        self.__button_8 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='8', command=lambda: self.__enter('8'))
        self.__button_9 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='9', command=lambda: self.__enter('9'))
        self.__button_multiply = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='*', command=lambda: self.__operation('*'))
        self.__button_clear.grid(row=2, column=0)
        self.__button_7.grid(row=2, column=1)
        self.__button_8.grid(row=2, column=2)
        self.__button_9.grid(row=2, column=3)
        self.__button_multiply.grid(row=2, column=4)
        self.__button_advanced = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='Advanced', command=self.__window_expand)
        self.__button_decimal = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='.', command=lambda: self.__enter('.'))
        self.__button_0 = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='0', command=lambda: self.__enter('0'))
        self.__button_sign = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='+/-', command=lambda: self.__enter('sign'))
        self.__button_divide = Button(self.__simple_grid, height=self.HEIGHT, width=self.WIDTH, text='/', command=lambda: self.__operation('/'))
        self.__button_advanced.grid(row=3, column=0)
        self.__button_decimal.grid(row=3, column=1)
        self.__button_0.grid(row=3, column=2)
        self.__button_sign.grid(row=3, column=3)
        self.__button_divide.grid(row=3, column=4)

        self.__advanced_grid = Frame(self.__window)
        self.__advanced_grid.grid(row=1, column=1)
        self.__button_pow = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='^', command=lambda: self.__operation('^'))
        self.__button_sqrt = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='sqrt', command=lambda: self.__single_op('sqrt'))
        self.__button_sin = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='sin', command=lambda: self.__single_op('sin'))
        self.__button_pow.grid(row=0, column=0)
        self.__button_sqrt.grid(row=0, column=1)
        self.__button_sin.grid(row=0, column=2)
        self.__button_square = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='x^2', command=lambda: self.__single_op('2'))
        self.__button_cbrt = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='cbrt', command=lambda: self.__single_op('cbrt'))
        self.__button_cos = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='cos', command=lambda: self.__single_op('cos'))
        self.__button_square.grid(row=1, column=0)
        self.__button_cbrt.grid(row=1, column=1)
        self.__button_cos.grid(row=1, column=2)
        self.__button_inverse = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='x^-1', command=lambda: self.__single_op('-1'))
        self.__button_ln = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='ln', command=lambda: self.__single_op('ln'))
        self.__button_tan = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='tan', command=lambda: self.__single_op('tan'))
        self.__button_inverse.grid(row=2, column=0)
        self.__button_ln.grid(row=2, column=1)
        self.__button_tan.grid(row=2, column=2)
        self.__button_mod = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='Modulus', command=lambda: self.__operation('%'))
        self.__button_log = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='log', command=lambda: self.__single_op('log'))
        self.__button_fact = Button(self.__advanced_grid, height=self.HEIGHT, width=self.WIDTH, text='!', command=lambda: self.__single_op('!'))
        self.__button_mod.grid(row=3, column=0)
        self.__button_log.grid(row=3, column=1)
        self.__button_fact.grid(row=3, column=2)

        self.__advanced_grid.grid_forget()
   

    def __all_clear(self) -> None:
        '''
        Clears the calculator's view screen as well as the stored numbers from previous entries
        '''
        self.__clear()
        self.__num_stored = ''


    def __clear(self) -> None:
        '''
        Clears the calculator view screen and any numbers entered since the last operation
        '''
        self.__num_shown = '0'
        self.__replace_main_entry()


    def __enter(self, pressed: str) -> None:
        '''
        Handles button input for buttons that enter digits, decimal points or sign changes
        :param pressed: The pressed button on the calculator that corresponds with an entered character
        '''
        if self.__is_new_number and not pressed == 'sign': # Starts on the second number of an equation if applicable
            self.__num_stored = self.__num_shown
            self.__num_shown = '0'
            self.__is_new_number = False
        if pressed.isdigit(): # Chooses the correct way to enter the given input
            self.__num_shown = self.__num_shown + pressed if self.__num_shown != '0' else pressed
        elif pressed == 'sign':
            self.__num_shown = '-' + self.__num_shown if self.__num_shown[0] != '-' else self.__num_shown[1:]
        elif pressed == '.':
            if '.' not in self.__num_shown:
                self.__num_shown += '.'
        self.__replace_main_entry()


    def __operation(self, pressed) -> None:
        '''
        Designates the operator to be used based on user input
        :param pressed: The user's chosen operation
        '''
        if self.__num_stored != '': # The calculator will first evaluate an operation if needed
            self.__evaluate()
        if self.__operator != pressed:
            self.__operator = pressed
        self.__is_new_number = True # Signals to future number entries that a new number is being entered


    def __single_op(self, pressed) -> None:
        '''
        Handles processing the math for operations on one number
        :param pressed: The user's chosen operation
        '''
        if self.__num_stored != '': # The calculator will first evaluate an operation if needed
            self.__evaluate()
        operating_num = float(self.__num_shown)
        result = operating_num
        try: # Possible errors during runtime: ZeroDivisionError (0^-1), ValueError (log(<0), OverflowError (10^1000))
            if pressed == '2': # Math for each operator depending on the user's choice
                result = operating_num ** 2
            elif pressed == '-1':
                if math.fabs(operating_num) < 1E-10:
                    raise ZeroDivisionError
                else:
                    result = operating_num ** -1
            elif pressed == 'sqrt':
                if operating_num < 1E-10:
                    raise ValueError
                else:
                    result = math.sqrt(operating_num)
            elif pressed == 'cbrt':
                result = math.cbrt(operating_num)
            elif pressed == '!':
                result = math.factorial(int(operating_num))
            elif pressed == 'ln':
                if operating_num < 1E-10:
                    raise ValueError
                else:
                    result = math.log(operating_num)
            elif pressed == 'log':
                if operating_num < 1E-10:
                    raise ValueError
                else:
                    result = math.log10(operating_num)
            elif pressed == 'sin':
                result = math.sin(operating_num)
            elif pressed == 'cos':
                result = math.cos(operating_num)
            elif pressed == 'tan':
                result = math.tan(operating_num)
            self.__num_shown = str(result)
            self.__operator = ''
            self.__replace_main_entry()
        except ZeroDivisionError: # Errors result in displaying an error message to the calculator display
            self.__show_error()
        except ValueError:
            self.__show_error()
        except OverflowError:
            self.__show_error()
        self.__is_new_number = True # Signals to future number entries that a new number is being entered


    def __evaluate(self) -> None:
        '''
        Handles the math for operations on two numbers, used by the operation function and linked to the = button on the calculator
        '''
        try: # Possible errors during runtime: ZeroDivisionError (1/0), ValueError (log(<0), OverflowError (10^1000))
            if self.__num_stored == '': # Error checking in case an error causes __num_stored to be an empty string
                raise ValueError
            operating_num_1 = float(self.__num_stored)
            operating_num_2 = float(self.__num_shown)
            result = operating_num_2
            if self.__operator == '+': # Operator chosen based on user's choice
                result = operating_num_1 + operating_num_2
            elif self.__operator == '-':
                result = operating_num_1 - operating_num_2
            elif self.__operator == '*':
                result = operating_num_1 * operating_num_2
            elif self.__operator == '/':
                if -1E-10 < operating_num_2 < 1E-10:
                    raise ZeroDivisionError
                else:
                    result = operating_num_1 / operating_num_2
            elif self.__operator == '^':
                if -1E-10 < operating_num_2 < 1E-10 and -1E-10 < operating_num_1 < 1E-10:
                    raise ZeroDivisionError
                else:
                    result = math.pow(operating_num_1, operating_num_2)
            elif self.__operator == '%':
                result = operating_num_1 % operating_num_2
            self.__num_shown = str(result)
            self.__num_stored = ''
            self.__operator = ''
            self.__replace_main_entry()
        except ZeroDivisionError:
            self.__show_error()
        except OverflowError:
            self.__show_error
        except ValueError:
            self.__operator = ''
        self.__is_new_number = True


    def __show_error(self) -> None:
        '''
        Function for displaying errors to the calculator and continuing functionality afterwards
        '''
        self.__num_shown = '0'
        self.__num_stored = ''
        self.__main_entry.config(state=NORMAL)
        self.__main_entry.delete(0, END)
        self.__main_entry.insert(0, 'ERROR')
        self.__main_entry.config(state=DISABLED)


    def __replace_main_entry(self) -> None:
        '''
        Replaces the contents of the entry box in the calculator with updated values
        '''
        self.__main_entry.config(state=NORMAL)
        self.__main_entry.delete(0, END)
        if math.fabs(float(self.__num_shown)) < 1E10: # BUG- glitches out for large magnitude negative numbers
            self.__main_entry.insert(0, f'{float(self.__num_shown):.10f}'.rstrip('0').rstrip('.'))
        else:
            magnitude = math.floor(math.log10(math.fabs(float(self.__num_shown))))
            decimal_value = float(self.__num_shown) / math.pow(10, magnitude) 
            self.__main_entry.insert(0, f'{decimal_value}E{magnitude}')
        self.__main_entry.config(state=DISABLED)


    def __window_expand(self) -> None:
        '''
        Expands and contracts the calculator window depending on if the user wishes to use the simple or advanced version
        '''
        if not self.EXPANDED: # Toggles window size and visibility of advanced buttons
            self.__window.geometry("640x380")
            self.__button_advanced.config(text="Simple")
            self.EXPANDED = True
            self.__advanced_grid.grid(row=1, column=1)
        else:
            self.__advanced_grid.grid_forget()
            self.__window.geometry("400x380")
            self.__button_advanced.config(text="Advanced")
            self.EXPANDED = False
            
        
