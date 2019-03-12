'''
This module is for geometry shapes!
'''

def square(n):
    """ Returns the square value of n!"""
    return n*n


def triangle(n):
    """Returns the factorial of n!"""
    result = n
    while n > 0:
        result += n - 1
        n -= 1
    return result


def cube(n):
    """Returns the cube of n!"""
    return n * n * n