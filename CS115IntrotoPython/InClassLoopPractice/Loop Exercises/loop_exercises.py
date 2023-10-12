'''
@author:
Pledge:

Objective: To become familiar with imperative style and for and while loops.

# Search for "TODO" to find the incomplete functions.
'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 1
' Study function questify(). Then implement questifyAlt() so that it gives
' the same results as questify(), using map and lambda but no helping function.
' Hint: adapt the body of addQuestmark().
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from functools import reduce

def questify(str_list):
    '''Assume str_list is a list of strings. Returns a list of
    the same strings but with ? suffixed to each.'''
    def addQuestmark(s):
        '''Adds a question mark to a string.'''
        return s + '?'

    return list(map(addQuestmark, str_list))

def questifyAlt(str_list):
    '''Same as questify'''
    output = []
    for word in str_list:
        output.append(word + '?')
    return output

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 2
' Study functions leppard() and catenate(). Implement catenateLoop(), without
' using recursion or reduce or any built-in Python function. Instead, use a
' loop. In some ways your code will resemble the body of leppard().
' If you prefer, you can follow the style of leppardIndex(), but I suggest not.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def leppard(inputString):
    '''Mystery.'''
    outputString = ''
    for symbol in inputString:
        if symbol == 'o':
            outputString = outputString + 'ooo'
        else:
            outputString = outputString + symbol
    print(outputString)

def leppardIndex(inputString):
    '''Same as leppard(), but using an integer index rather than directly
    referring to elements of the input string.'''
    outputString = ''
    for i in range(len(inputString)):
        if inputString[i] == 'o':
            outputString = outputString + 'ooo'
        else:
            outputString = outputString + inputString[i]
    print(outputString)

def catenate(str_list):
    '''Assume str_list is a list of strings.
    Return a single string, their catenation.'''
    if str_list == []:
        return ''
    return reduce(lambda s, t: s + t, str_list)

def catenateLoop(str_list):
    '''Same as catenate'''
    output = ''
    for word in str_list:
        output += word
    return output

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 3
' Implement letterScoreLoop using --you guessed it-- a loop instead of
' recursion. Also, do not use map or reduce.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
scrabbleScores = [["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], \
                  ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], \
                  ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], \
                  ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], \
                  ["y", 4], ["z", 10]]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", \
               "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist):
    '''Assume scorelist is a list of lists [ltr, val] where ltr is a single
    letter and val is a natural number. Assume letter is a single letter string,
    that occurs in scorelist. Return the associated value.'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def letterScoreLoop(letter, scorelist):
    '''Same as letterScore'''
    # HINTS: You can rely on the assumption that letter occurs in scorelist.
    # It may be helpful to use an if-statement without an else.
    for item in scorelist:
        if letter == item[0]:
            return item[1]

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 4
' Implement wordScoreLoop using a loop instead of recursion. (And don't
' use map or reduce.)
' Use letterScore() or letterScoreLoop(); it shouldn't matter which one.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordScore(S, scorelist):
    '''Assume S is a string and scorelist is in the format above and
    includes every letter in S. Return the scrabble score of that string.'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordScoreLoop(S, scorelist):
    '''Same as wordScore'''
    value = 0
    for letter in S:
        value += letterScoreLoop(letter, scorelist)
    return value

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 5
' Implement wordsWithScoreLambda using a lambda instead of the helper scoreWord.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''Assume dct is a list of words and scores is a list of [letter, number]
    pairs. Return a copy of the dictionary, annotated so each word is paired
    with its value. For example, wordsWithScore(scrabbleScores, aDictionary)
    should return [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''
    def scoreWord(wrd):
        return [ wrd, wordScore(wrd, scores) ]

    return list(map(scoreWord, dct))

def wordsWithScoreLambda(dct, scores):
    '''Same as wordsWithScore'''
    pass

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 6
' Implement wordsWithScoreLoop using a loop instead of map or recursion.
' Be careful NOT to change the dictionary.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScoreLoop(dct, scores):
    '''Same as wordsWithScore'''
    output = []
    for item in dct:
        output.append([item, wordScoreLoop(item, scores)])
    return output
