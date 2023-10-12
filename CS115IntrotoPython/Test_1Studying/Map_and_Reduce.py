def dbl(n):
    return 2 * n

def add(x, y):
    return x + y

def evens(n):
    """
    Input: A positive integer
    Output: The fist n even nonegative integres
    """
    return list(map(dbl, range(n)))

from functools import reduce
def span(L):
    """
    Input: A list of numbers
    Output: The difference between the largest and smallest numbers in the list
    """
    return reduce(max, L) - reduce(min, L)

def gauss(n):
    """
    Input: A positive integer
    Output: The sum of all positive integres up until that integer inclusive
    """
    return reduce(add, range(1, n + 1))

def sumOfSquares(N):
    """
    Input: A positive integer
    Output: The sum of the squares of each integer up until that integer inclusive
    """
    return reduce(add, map(lambda x: x ** 2, range(1, N + 1)))
