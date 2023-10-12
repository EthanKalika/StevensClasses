#Name: Ethan Kalika
#Pledge: "I pledge my Honor that I have abided by the Stevens Honor System"

################
# Kung Fu Panda has a number of staircases he needs to climb.
# He likes to climb each staircase 1, 2, or 3 steps at a time.
# Being a very precocious character, he wonders how many ways
#there are to reach the top of the staircase. Your help is needed here.
################

# 1. Write a recursive function KFP_slow that will take as an input a positive integer
#    denoting the number of stairs and will return the number of ways Kung Fu Panda can climb those stairs.


def KFP_slow(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        three = KFP_slow(n - 3)
        two = KFP_slow(n - 2)
        one = KFP_slow(n - 1)
        return one + two + three

print(KFP_slow(5))
print(KFP_slow(30))


# 2. Use memoization to speed up your solution of KFP_slow.
memo = {}
def KFP_fast(n):
    if (n) in memo:
        return memo[(n)]
    elif n <= 0:
        memo[(n)] = 0
        return memo([n])
    elif n == 1:
        memo[(n)] = 1
        return memo[(n)]
    elif n == 2:
        memo[(n)] = 2
        return memo[(n)]
    elif n == 3:
        memo[(n)] = 4
    else:
        three = KFP_fast(n - 3)
        two = KFP_fast(n - 2)
        one = KFP_fast(n - 1)
        memo[(n)] = one + two + three
        return memo[(n)]

print(KFP_fast(5))
print(KFP_fast(30))

