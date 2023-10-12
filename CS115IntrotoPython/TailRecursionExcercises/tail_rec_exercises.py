# tail recursion exercise 

# Complete the following exercises on paper and pencil.
# Check your work by transferring your solutions to your computer
# Here's an example we already studied.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def factorial_alt(n, a = 1):
    if n == 0:
        return a
    else:
        return factorial_alt(n-1, a*n)

def test_factorial():
    assert factorial(5) == factorial_alt(5)
    assert factorial(120) == factorial_alt(120)
    assert factorial(0) == factorial_alt(0)
    assert factorial(1) == factorial_alt(1)

#Exercise 0: Here is a recursive function
#Implement the alternate version, using tail recursion
def exp(n,k):
    '''n**k, assuming k>=0 and n is a number'''
    if k == 0:
        return 1
    else:
        return n*exp(n, k-1)

def exp_alt(n,k, a = 1):
    '''n**k, assuming k>=0 and n is a number'''
    if k == 0:
        return a
    else:
        return exp_alt(n, k - 1, a * n)
    
def test_exp():
    assert exp(4,3) == exp_alt(4,3)
    assert exp(5,2) == exp_alt(5,2)

# Exercise 1: Here's another recursive function.
# Implement the alternate version, using tail recursion.
def sumSq(L):
    '''Assuming L is a list of numbers, return the sum of their squares.'''
    if L==[]: return 0
    else: return L[0]**2 + sumSq(L[1:])
    
def sumSq_alt(L, a = 0):
    if L == []:
        return a
    else:
        return sumSq_alt(L[1:], a + L[0] ** 2)

def test_sumsq():
    t0 = [2,4]
    t1 = list(range(5))
    assert sumSq(t0) == sumSq_alt(t0)
    assert sumSq(t1) == sumSq_alt(t1)
    

# Exercise 2: Here's another recursive function.
# Implement the alternate version, using tail recursion.

def copies(n, ls):
    '''assuming ls is a list of letters, of length at least n,
    return a list with n copies of the first, n-1 copies of the
    second, etc.  Don't include zero copies.'''
    if n <= 0: return []
    else: return [(n*ls[0])] + copies(n-1, ls[1:])

def testCopies():
    assert copies(3,['a','b','c','d']) == ['aaa', 'bb', 'c']

def copies_alt(n, ls, a = []):
    if ls == [] or n <= 0:
        return a
    else:
        return copies_alt(n - 1, ls[1:], a + [(n * ls[0])])

def testCopiesAlt():
    L = ['a','b','c','d']
    assert copies_alt(3,L) == copies(3,L)
    assert copies_alt(2,L) == copies(2,L)
