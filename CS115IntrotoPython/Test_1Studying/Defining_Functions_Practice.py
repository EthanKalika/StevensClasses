def addTwoDigits(n):
    """
    Input: A two digit number
    Output: The sum of the two digits
    """
    return n % 10 + n // 10

def largestNumber (n):
    """
    Input: An integer
    Ouput: The largest number with that many integers
    """ 
    return 10 ** n - 1

def reverse(l):
    """
    Input: A list
    Output: The revers of that list
    """
    return l[::-1]

def headtail(n):
    """
    Input: An integer greater than 10
    Output: A list conatining the squares of teh first 5 numbers and the last five numbers before the given number
    """
    return list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, n - 4, n - 3, n - 2, n - 1, n]))

from functools import reduce
def longestString(l):
    """
    Input: A list of strings
    Output: The length of the longest string in the list
    """
    return reduce(max, map(len, l))

def add(x, y):
    """
    Input: Two numbers
    Output: Their sum
    """
    return x + y

import math
def inverseSquaresSum(n):
    """
    Input: An integer n
    Output: The sum of the inverse squares of every number between 1 and the given number
    """
    return reduce(add, map(lambda x: 1 / math.sqrt(x), range(1, n + 1)))

"""
Notes:
Rememebr that to use the sqare root function and pi you must import the math class
To call the square root function you must say math.sqrt()
To call the pi function you must call math.pi()
You can not use the sum built in fuction with higher order functions
    TO avoid this problem you must code an addition helper function
"""
