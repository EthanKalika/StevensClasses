'''
Created on 3 / 9 / 22
@author:   Ethan Kalika and Caitlin McLaughlin
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

from functools import reduce
'''
def row(S):
    '''
'''
    Input: A string S
    Ouput: An integer representing how many identicle characters in a row are at the start of S
    '''
'''
    if S == '':
        return 0
    elif len(S) == 1 or not S[0] == S[1]:
        return 1
    return 1 + row(S[1:])

def compressWithoutFirst(S):
    """
    Input: A binary string of 64 bits
    Output: A run-length encoding of the string
    Note: If the string begins with 1's then this function will not start the runlength encoding with a 0, the 0 will be inserted by the next function
    """
    if S == '':
        return []
    return [row(S)] + compressWithoutFirst(S[row(S):])
'''
    
def base2Converter(n):
    """
    Input: An integer n
    Output: The binary representation of n (as a string)
    """
    if n == 0:
        return ''
    elif n % 2 == 1:
        return base2Converter(n // 2) + "1"
    return base2Converter(n // 2) + "0"

def adjustLength(n):
    '''
    Input: An integer n
    Output: A binary representation of n using COMPRESSED_BLOCK_SIZE number of bits
    '''
    if len(base2Converter(n)) >= COMPRESSED_BLOCK_SIZE:
        return base2Converter(n)[:COMPRESSED_BLOCK_SIZE]
    else:
        return '0' * (COMPRESSED_BLOCK_SIZE - len(base2Converter(n))) + base2Converter(n)

def countOneBit(S, bit):
    '''
    Input: A binary string and a bit value (the bit value is given as an integer)
    Output: The number of that bit that comes at the beginning of the string
    '''
    if S == '' or not int(S[0]) == bit:
        return 0
    return 1 + countOneBit(S[1:], bit)

def compressHelp(S, bit, COMPRESSED_BLOCK_SIZE):
    '''
    Input: A binary string, an integer bit value, and a number of bit that should be used to represent every block of similar integers
    Output: A list containing all the lengths of consecutive common integers
    '''
    if S == '':
        return []
    x = countOneBit(S[:MAX_RUN_LENGTH], bit)
    return [x] + compressHelp(S[x:], 1 - bit, COMPRESSED_BLOCK_SIZE)

def addStrings(x, y):
    '''
    Input: Two strings
    Output: The sum of the two strings
    '''
    return x + y

def compress(S):
    """
    Input: A binary string of 64 bits
    Output: A run-length encoding of the string
    Question 1: The largest possible number of bits that this function can use to encode a 64 bit string is 325. This will happen when the given string is an alternating string of 1's and 0's that
    starts with a 1.
    """
    return reduce(addStrings, map(adjustLength, compressHelp(S, 0, COMPRESSED_BLOCK_SIZE)))

def binaryToDecimal(S):
    '''
    Input: A binary string
    Output: The decimal number corresponding to this string
    '''
    if S == '':
        return 0
    return 2 ** (len(S) - 1) * (int(S[0])) + binaryToDecimal(S[1:])

def uncompress(C):
    '''
    Input: A run-length encoding of a string
    Output: The original string
    '''
    if len(C) < COMPRESSED_BLOCK_SIZE:
        return ''
    return '0' * binaryToDecimal(C[0:COMPRESSED_BLOCK_SIZE]) + '1' * binaryToDecimal(C[COMPRESSED_BLOCK_SIZE:2 * COMPRESSED_BLOCK_SIZE]) + uncompress(C[2 * COMPRESSED_BLOCK_SIZE:])

def compression(S):
    '''
    Input: A binary string
    Output: The ratio of the original string length to its compressed size
    '''
    return len(compress(S)) / len(S)

#Test 1: Compression on the image '01010101010101010101' returned 5.0
#Test 2: Compression on the image "10001" returned 4.0
#Test 3: Compression on the image '0001100000111100001111000011110001111110111111110011110000100100' returned 1.484375
#Test 4: Compression on the image "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8 returned 1.328125
#Test 5: Compression on the image "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0" returned 1.015625
#Test 6: Compression on the image 16 * '0' + 16 * '1' + 16 * '0' + 16 * '1' returned 0.3125
#Test 7: Compression on the image '1' * 47 + '0' * 17 returned 0.390625
#Test 8: Compression on the image '10' * 32 returned 5.078125

'''
Prove or disprove that there exists a function that maps every element of the set of all 64 bit binary strings to a unique element of the set of all binary strings whose length is less than 64.
Disproof by contradiction. Lets make the supposition that there was a function that could map every element of the set of all 64 bit binary strings to a unique element of the set of all binary strings
whose length is less than 64.
The set of all binary strings that are 64 bits long consists of 2^64 elements. The set of all binary strings whose length is less than 64 bits contains 2^63 + 2^62 + ... + 2^1 + 2^0 elements. That is
2^64 - 1 elements.
Therefor the function must map each of 2^64 elements to a unique element in a set of only 2^64 - 1 of them.
Therefor by the pigeon hole principle the function must map atleast 2 elements from the first set to atleast 1 element from the second set.
But it was said prior that the function must map every element from the first set to a unique element in the second.
Therefor the suposition that such a function exists leads logically to a contradiction and must be false.
Therefor there does not exist a function that can compress every 64 bit string to a string with 63 or less bits.
'''
