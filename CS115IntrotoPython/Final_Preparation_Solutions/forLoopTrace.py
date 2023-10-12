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
# The loop changes L, s, and i, so we make a table
# of their values.  For the call squareSumsTrace(5)
# it looks like this:

#  s  i  L 
#  ----------------------
#  0 1 []
#  1 2 [1]
#  5 3 [1, 5]
#  14 4 [1, 5, 14]
#  30 5 [1, 5, 14, 30]
#  55 5 [1, 5, 14, 30, 55]


# Below fill in the squareSumsTrace function as a self-tracing version of square Sums

def squareSumsTrace(n):
    '''self-tracing version of squareSums'''
    #TODO
    L = []
    s = 0
    print("s\ti\tL")
    print("-----------------------------")
    
    for i in range(1,n+1):
        print(str(s) + "\t" + str(i) +"\t"+ str(L))
        s += i*i
        L.append(s)
    print(str(s) + "\t"+ str(i) +"\t" + str(L))
    return L
