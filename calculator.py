"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b): # use math library/raise ValueError
    if a <= 0 or b <= 0:
        raise ValueError("Input must be greater than 0")
    return math.log(b,a)

def exponent(a, b):
    return a**b




