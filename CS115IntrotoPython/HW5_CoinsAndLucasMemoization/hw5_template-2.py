'''
Created on 3 / 2 / 22
@author:   Ethan Kalika
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 5 
'''

memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[(n)]
    elif n == 0:
        memo[(0)] = 2
        return memo[(0)]
    elif n == 1:
        memo[(1)] = 1
        return memo[(1)]
    else:
        memo[(n - 1)] = fast_lucas(n - 1)
        memo[(n - 2)] = fast_lucas(n - 2)
        memo[(n)] = memo[(n - 1)] + memo[(n - 2)]
        return memo[(n)]

memo1 = {}
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    coins = tuple(coins)
    if (amount, coins) in memo1:
        return memo1[(amount, coins)]
    elif amount == 0:
        memo1[(amount, coins)] = 0
        return memo1[(amount, coins)]
        return 0
    elif len(coins) == 0 or amount < 0:
        memo[(amount, coins)] = float('inf')
        return memo[(amount, coins)]
    else:
        use_it = 1 + fast_change(amount - coins[0], coins)
        loose_it = fast_change(amount, coins[1:])
        memo1[(amount, coins)] = min(use_it, loose_it)
        return memo1[(amount, coins)]

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


