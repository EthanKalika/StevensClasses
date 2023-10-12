###########################################################################
# RULES: You can use the following:
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
# Name and pledge: Ethan Kalika
# "I pledge my honor that I have abided by the Stevens Honor System"
#
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok
# There should be no error.
###########################################################################

print("So far so good...")

###########################################################################
# Question 1 (20 points) [assess: encoding]
# This table defines a boolean function, f, of three arguments.
#
#    x | y | z | f(x,y,z)
#    --------------------
#    0 | 0 | 0 | 0
#    0 | 0 | 1 | 0
#    0 | 1 | 0 | 0
#    0 | 1 | 1 | 1
#    1 | 0 | 0 | 1
#    1 | 0 | 1 | 0
#    1 | 1 | 0 | 0
#    1 | 1 | 1 | 1        
# 
# Complete the following Python implementation of f, using a single return.
# Use the built-in Python functions "and", "or", "not".
# Hint: use the minterm expansion principle.
###########################################################################

def f(x, y, z):
    return (not x and y and z) or (x and not y and not z) or (x and y and z)



###########################################################################
# Question 2: (20 points) [assess: encoding]
# Part A: What is the two's complement representation of 29 in six bits?
# 
#    A: 011111 
#    B: 000111
#    C: 011101   
#    D: 000101
#
# ANSWER = C
#
###########################################################################
# Part B: What is the two's complement representation of -23 in six bits?
#
#    A: 101001
#    B: 110110
#    C: 110111
#    D: 010111
#
# ANSWER = A
#
###########################################################################
# Part C: Using two's complement with six bits, what is the largest
# positive number that can be represented, and what is the smallest (most negative)?
#
# LARGEST = 63            your answer, in base ten
# 
# SMALLEST = -64           your answer, in base ten
#
###########################################################################
# Part D: Write your answers from part C in two's complement with six bits.
#
# LARGEST = 111111            your answer, in binary
# 
# SMALLEST = 000001           your answer, in binary
#
############################################################################ 


###########################################################################
# Question 3: (20 points) [assess: coding]
# Complete the following function, using recursion on the lists.  That means 
# you can only access L using the expressions L[0], L==[], and L[1:].  And
# the same for M.  
#
# Hint: It can be done with one recursive call, where both lists are smaller.
###########################################################################

def listProd(L,M):
    '''Assume L and M are lists of  numbers.  Return a list of their products
    at corresponding indexes.  If one list is longer than the other, include its 
    elements at the end.  See testProd for examples.'''
    if L == [] and M == []:
        return []
    if M == []:
        return [L[0]] + listProd(L[1:], M)
    if L == []:
        return [M[0]] + listProd(L, M[1:])
    return [L[0] * M[0]] + listProd(L[1:], M[1:])

def testProd():
    assert listProd([1,2,3], [1,2,3]) == [1, 4, 9]
    assert listProd([1,5,1], [2,3,3]) == [2,15,3]
    assert listProd([], [1,3,5,7]) == [1,3,5,7]
    assert listProd([1,2,3], [6,5,4,9,8,7]) == [6,10,12,9,8,7]


###########################################################################
# Question 4: (20 points) [assess: design]
# Below is an implementation of the longest common subsequence function.
# Add memoization, which will make it more efficient.  
  
# Hint: create the dictionary outside the function, so you can refer to it
# in the code you add to LCS.
###########################################################################

memo = {}

def LCS(S1,S2):
    '''Length of the longest common subsequence of strings S1, S2.'''
    if (S1, S2) in memo:
        return memo[S1, S2]
    elif S1 == "" or S2 == "":
        memo[S1, S2] = 0
        result = memo[S1, S2]
    elif S1[0] == S2[0]:
        memo[S1, S2] = 1 + LCS(S1[1:], S2[1:])
        result = memo[S1, S2]
    else:
        memo[S1[1:], S2] = LCS(S1[1:], S2)
        memo[S1, S2[1:]] = LCS(S1, S2[1:])
        chopS1 = memo[S1[1:], S2]
        chopS2 = memo[S1, S2[1:]]
        result = max(chopS1, chopS2)
    return result



def testLCS():
    assert LCS("sam","spam!") == 3
    assert LCS("veto", "vote") == 2
    assert LCS("tranquil", "trail") == 5


###########################################################################
# Question 5: (15 points) [assess: execution]
# Write out the trace of function calls starting from fab(4,3) for the
# function defined below.
# Use indentation to indicate which calls are the result of preceding calls.
#
# Hint: You are welcome to modify the function and make it trace itself.
# But to answer the question you need to write your trace in the comment below.
###########################################################################

def fab(n,k):
    '''mystery function'''
    if n == 0 or n == 1:
        return k
    else:
        return fab(n-2,k) + fab(n-1,k)

'''
Your trace here:
fab(4, 3)
    fab(2, 3)
        fab(0, 3)
        fab(1, 3)
    fab(3, 3)
        fab(1, 3)
        fab(2, 3)
            fab(0, 3)
            fab(1, 3)
'''




