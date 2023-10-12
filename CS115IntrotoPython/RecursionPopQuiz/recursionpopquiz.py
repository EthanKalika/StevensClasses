# pop quiz Feb 11, 2022

# Name: Ethan Kalika
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"

# Implement this function so it works correctly.
# Use recursion  
# You may use the built-in max function, only to find the max of two numbers.
# Hint: The base case is a one-element list which you can check as len(L)==1.

def myMax(L):
    '''Assume L is a non-empty list of numbers.  Return the maximum value.'''
    if (len(L) == 1):
        return L[0]
    else:
        return max(L[0], myMax(L[1:]))

def test():
    '''Prints True for each successful test'''
    print( myMax([1,2,3]) == 3 )
    print( myMax([12,17,5,8,-100]) == 17 )
    print( myMax([12]) == 12 )

