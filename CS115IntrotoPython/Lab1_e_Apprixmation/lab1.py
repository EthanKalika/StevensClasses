############################################################
# Name:Ethan Kalika
# Pledge:I pledge my honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    """
    Input: a number n
    Output: a floating point number 1/n
    """
    #pass
    return 1/x


def addition(x, y):
    """
    Input: two numbers
    Output: sum of the two numbers
    """
    return x + y

def e(n):
    """
    Input: an number n
    Output: an (n + 1)th degree taylor polynomial approximation of e
    """
    #pass
    list1 = list(range(n+1))
    list2 = list(map(factorial, list1))
    list3 = list(map(inverse, list2))
    return reduce(addition, list3)


