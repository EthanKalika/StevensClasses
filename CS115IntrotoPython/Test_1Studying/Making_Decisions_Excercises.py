def abs(n):
    """
    Input: An integre
    Output: The absolute value of the integer
    """
    if n >= 0:
        return n
    else:
        return -1 * n

def maxOutThree(a, b, c):
    """
    Input: Three integers
    Output: The largest of the three integers
    """
    if a >= b:
        if a >= c:
            return a
        return c
    if b >= c:
        return b
    return c
    
def matchFirst(s1, s2):
    """
    Input: Two strings
    Output: A boolean that is true if and only if the first characters are the same
    """
    return s1[0] == s2[0]

def isPalindrome(s):
    """
    Input: A string
    Output: A boolean that is true if and only if the string is a palindrome
    """
    return s == s[::-1]

def rightTrianlgesCount(l):
    """
    Input: A list of lists containing three numbers each in assending order
    Ouput: An integer representing the amount of sublists that can represent the sides of a right triangle
    """
    return len(list(filter(lambda l1: l1[-1] ** 2 == (l1[0] ** 2 + l1[1] ** 2), l)))

def isRightTriangle(l):
    """
    Input: A list containing 3 numbers
    Output: A boolean that is true if and only if the three numbers can be sides of a right trianlge
    """
    if l[0] ** 2 == l[1] ** 2 + l[2] ** 2:
        return True
    elif l[1] ** 2 == l[0] ** 2 + l[2] ** 2:
        return True
    elif l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
        return True
    return False

def rightTrianlgesCountAdvanced(l):
    """
    Input: A list of lists containing three numbers
    Ouput: An integer representing the amount of sublists that can represent the sides of a right triangle
    """
    return len(list(filter(isRightTriangle, l)))

"""
Notes:
You only have to import "reduce" from the functools library not "filter" or any other higher order functions that we learned about
When writing out a boolean start with a capital letter
    "True" instead of "true" and "False" instead of "false"
"""
