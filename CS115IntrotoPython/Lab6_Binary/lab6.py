'''
Created on 3 / 3 / 2022
@author:   Ethan Kalika
Pledge:    "I pledge my Honor that I have abided by the Stevens Honor System"

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    #Question1: 101010
    return n % 2 == 1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.
    
    Question 2: If I am given an odd base 10 number the least significant bit in the base 2 representation will be a 1. If I am given an even base 10 number the least significant bit in the base 2
    representation will be 0.
    
    Question 3: By eliminating the last bit in the base 2 representation of a number we perform integer division by 2 on that number.

    Question 4: Given a base 10 representation of an integer N and a base 2 representation of Y which is the result of preforming integer dividion by 2 on N, then we can find the base 2 representation
    of N by appending a 0 at the end of Y if N is even and appending a 1 at the end of Y if N is odd.
    '''
    if n == 0:
        return ''
    elif n == 1:
        return '1'
    return numToBinary(n // 2) + str(n % 2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[0]) * 2 ** (len(s) - 1) + binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s[-1] == '0':
        return s[:-1] + '1'
    ourString = numToBinary(binaryToNum(s) + 1)
    length = len(ourString)
    if length < 8:
        return '0' * (8 - length) + ourString
    return ourString[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else:
        print(s)
        count(increment(s), n - 1)
    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.
    
    Question 5: The 81 is the smallest power of 3 that is larger that 59 so we go down to the next smallest power which is 27. 27 * 2 = 54 meaning that the first bit in the turnary representation will be 2 and
    will be in the 27's place. The next power down is 9 which does not fit because 59 - 54 = 5 < 9. So there will be a 0 in the 9's place. The next smallest power of 3 is 3, 3 fits into 5 once so the
    number in the three's place is 1. 5 - 3 = 2. This means that the number in the ones place must be 2.
    The ternary representation of 59 is: 2012
    '''
    if n == 0:
        return ''
    return numToTernary(n // 3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return int(s[0]) * 3 ** (len(s) - 1) + ternaryToNum(s[1:])
