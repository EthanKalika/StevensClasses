# fastLCS (DN last rev Oct 2020)

# LCS as in the book

def LCS(S1, S2):
    """Length of longest common subsequence."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

# same as LCS, but "refactored", i.e., rewritten to make it easier to adapt

def LCSX(S1, S2):
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]: 
        return 1 + LCSX(S1[1:], S2[1:])
    else:
        chopS1 = LCSX(S1[1:], S2)
        chopS2 = LCSX(S1, S2[1:])
        answer = max(chopS1, chopS2)
        return answer


# Now comes the one that uses memoization to avoid redundancy.

memo = {}  # dictionary for use in fastLCS; keys are tuples (str1,str2)

def fastLCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    if S1 == '' or S2 == '':
        memo[(S1, S2)] = 0
        return 0
    elif S1[0] == S2[0]:
        memo[(S1[0], S2[0])] = 1
        memo[(S2[0], S1[0])] = 1
        return 1 + fas

import time
def testLCS(S1, S2):
    '''Check that fastLCS agrees with LCS; return true if so, else false.
    Try this with longish strings to get an idea of the difference in timing.'''
    print("S1 is ", S1, " S2 is ", S2)
    print("Using LCS - be patient")
    start = time.time()
    slow = LCS(S1,S2)
    print("Using LCS takes", time.time() - start)
    print("Using fastLCS")
    start = time.time()
    fast = fastLCS(S1,S2)
    print("Using LCS takes", time.time() - start)
    print("Slow result ", slow, "fast result ", fast)
    return "Done"

def test(): 
    print(testLCS("Are we done yet?", "Are birds in flight"))

def test2():
    print(testLCS("trending on twitter", "coronavirus"))




