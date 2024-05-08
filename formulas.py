from random import choice
from sys import exit


def add(values):
    sum = 0
    for i in values:
        if i < 0:
            sum += i
    return sum

def subtract(values):
    difference = 0
    modifier = 1
    for i in values:
        if i > 0:
            difference += modifier * i
            modifier = -1
    return difference

def multiply(values):
    product = 1
    checker = False
    for i in values:
        if i != 0:
            product *= i
            checker = True
    if checker:
        return product
    else:
        return 0
    
def divide(values):
    quotient = values[0]
    for i in values[1:]:
        if i != 0:
            quotient /= i
        else:
            exit("Cannot divide by 0")
    return quotient

def choose(values):
    return choice(values)