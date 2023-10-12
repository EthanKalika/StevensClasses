#Ethan Kalika
#"I pledge my honor that I have abided by the Stevens Honor System."

def dot(L, K):
    """
    Input: Two lists (assumed to be of the same length
    Output: Their dot product
    """
    if L == [] or K == []:
        return 0
    return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """
    Input: A string
    Ouput: A list of all the indevidual characters in the string
    """
    l = []
    if S == "":
        return l
    return l + [S[0]] + explode(S[1:])

def ind(e, L):
    """
    Input: An element and a sequence wehre a sequence refers to a string or a list
    Output: The index in the list or string where the element is first found
    """
    if L == [] or L == "" or L[0] == e:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    """
    Input: An element and a list
    Output: Another list that has all top-level instances of that element removed
    """
    if L == []:
        return L
    if L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])

def myFilter(boolean, L):
    """
    Input: A boolean value and a list
    Output: A new list that contains only the elements for which the boolean is true
    """
    if L == []:
        return L
    if boolean(L[0]):
        return [L[0]] + myFilter(boolean, L[1:])
    else:
        return myFilter(boolean, L[1:])

def deepReverse(L):
    """
    Input: A list that may contain other lists
    Output: A list which is the reverse of the input including all the inner lists
    """
    if L == []:
        return[]
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
