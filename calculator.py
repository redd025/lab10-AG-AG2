"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_roots(a):
    if a<0:
        raise ValueError("Input must be positive")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a,b)

def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Input must be greater than 0")
    return math.log(b,a)

def exponent(a, b):
    return a**b




