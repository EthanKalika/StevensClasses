# Example showing how to trace a for-loop

def squareSums(n):
    '''list of the first n sums of squares'''
    L = []
    s = 0
    for i in range(1,n+1):
        s += i*i
        L.append(s)
    return L

# Draw the loop trace for squareSums


# Below fill in the squareSumsTrace function as a self-tracing version of square Sums

def squareSumsTrace(n):
    '''self-tracing version of squareSums'''
    L = []
    s = 0
    print('L\ts')
    print(L, '\t', s)
    for i in range(1, n + 1):
        s += i * i
        L.append(s)
        print(L, '\t', s)
    return L
