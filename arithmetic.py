"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    sums = num1+num2
    #print(sums)
    return sums


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    final = num1 - num2
    return final


def multiply(num1, num2):
    """Multiply the two inputs together."""
    final = num1*num2
    return final


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    final = num1/num2
    return final


def square(num1):
    """Return the square of the input."""
    return num1**2


def cube(num1):
    """Return the cube of the input."""
    return num1**3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1**num2


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1%num2

def add_mult(num1,num2,num3):
    final = (num1 + num2)*num3
    return final

def add_cubes(num1, num2):
    cube = num1**3 + num2**3
    print(cube)
    return cube
