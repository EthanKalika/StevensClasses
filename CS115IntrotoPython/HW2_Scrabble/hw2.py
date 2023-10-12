'''
Created on 2/9/22
@author:   Ethan Kalika
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

from functools import reduce
from dict import *
from bigdict import *

def letterScore(letter, scorelist):
    """
    Input: a letter and a list of lists containing letters and their associated scrabble scores
    Output: the score associated with the given letter
    This function will crash if the given letter is not associated with a scrabble score
    """
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """
    Input: a string of lowercase letters and a list of lists containing letters and their associated scrabble scores
    Output: the scrabble score associated with that word
    """
    if S == "":
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def isLetterInList(Rack, letter):
    """
    Input: a list and a letter
    Output: True if the letter is in the string and false if it is not

    This function is used in canBeAssembled
    """
    if Rack == []:
        return False
    elif Rack[0] == letter:
        return True
    else:
        return isLetterInList(Rack[1:], letter)

def removeLetter(Rack, letter):
    """
    Input: a list of lowercase letters and a letter
    Output: another list containing the first, but with the first instance of the given letter removed. If the letter is not in the list then the same list is returned

    This function is used in canBeAssembled
    """
    if isLetterInList(Rack, letter):
        if Rack[0] == letter:
            return Rack[1:]
        else:
            return  [Rack[0]] + removeLetter(Rack[1:], letter)
    return Rack

def canBeAssembled(Rack, S):
    """
    Input: a Rack (list of lowercase letters) and a string of lowercase letters
    Output: returns a true if S can be made with the letters in Rack and false if not
    
    This function is used in scoreList
    """
    if S == "":
        return True
    elif isLetterInList(Rack, S[0]):
        return canBeAssembled(removeLetter(Rack, S[0]), S[1:])
    else:
        return False

def scoreList(Rack):
    """
    Input: a Rack (list of lowercase letters)
    Output: A list containing all possible lists of words that can be assembled from the letters in Rack and their corresponding scrabble scores
    """
    l1 = list(filter(lambda x: canBeAssembled(Rack, x), Dictionary))
    return list(map(lambda x: [x, wordScore(x, scrabbleScores)], l1))

def decider(list1, list2):
    """
    Input: Two lists whose last element is a number
    Output: The list with the greater second number
    """
    if list1[1] > list2[1]:
        return list1
    return list2

def bestWord(Rack):
    """
    Input: a list of lowercase letters
    Output: a list containing the word with the greatest scrabble score, and its score
    """
    if len(scoreList(Rack)) == 0:
        return ["", 0]
    return list(reduce(decider, scoreList(Rack)))
