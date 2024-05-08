import math

def circle(radius):
    radius = float(radius)
    if radius <= 0:
        raise TypeError
    return math.pi * math.pow(radius, 2)


def square(side):
    side = float(side)
    if side <= 0:
        raise TypeError
    return math.pow(float(side), 2)


def rectangle(side1, side2):
    side1 = float(side1)
    side2 = float(side2)
    if side1 <= 0 or side2 <= 0:
        raise TypeError
    return side1 * side2


def triangle(side1, side2):
    side1 = float(side1)
    side2 = float(side2)
    if side1 <= 0 or side2 <= 0:
        raise TypeError
    return side1 * side2 / 2