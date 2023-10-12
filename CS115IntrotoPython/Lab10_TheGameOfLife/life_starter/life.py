#
# life.py - Game of Life lab
#
# Name: Ethan Kalika
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """
    Input: Two integers (one representing the width and one representing the height)
    Output: A two dimensional list containting only 0's and having width columns and height rows
    """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

import sys 
 
def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height): 
    """ creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w, h):
    """
    Input: A width and a height which are integers
    Output: A board which is all ones except for the boarders and has width columns and height rows
    """
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if not(row == 0 or row == h - 1 or col == 0 or col == w - 1):
                A[row][col] = 1
    return A

def randomCells(w, h):
    """
    Input: Two integers one representing the width and the second representing the height
    Output: A 2-D list with width columns and height rows where all cells are either 0's or 1's and are of random parity except for the boarders which are all 0's
    """
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if not(row == 0 or row == h - 1 or col == 0 or col == w - 1):
                A[row][col] = random.choice([0, 1])
    return A

def copy(A):
    """
    Input: A 2-D array called A
    Output: An exact copy of the array that is stored in a different place in memory
    """
    w = len(A[0])
    h = len(A)
    B = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if A[row][col] == 1:
                B[row][col] = 1
    return B

def innerReverse(A):
    """
    Input: A 2-D array called A
    Output: A new 2-D array that has 0's where the previos one had 1's and 1's where the previous 1 had 0's
    """
    B = copy(A)
    h = len(B)
    w = len(B[0])
    for row in range(h):
        for col in range(w):
            B[row][col] = 1 - B[row][col]
            if row == 0 or row == h - 1 or col == 0 or col == w - 1:
                B[row][col] = 0
    return B

def next_life_generation( A ): 
    """ makes a copy of A and then advanced one 
        generation of Conway's game of life within 
        the *inner cells* of that copy. 
        The outer edge always stays 0. 
    """
    B = copy(A)
    h = len(B)
    w = len(B[0])
    for row in range(h):
        for col in range(w):
            if col == 0 or col == w - 1 or row == 0 or row == h - 1:
                B[row][col] = 0
            else:
                count = countNeighbors(row, col, A)
                if count < 2 or count > 3:
                    B[row][col] = 0
                elif count == 3:
                    B[row][col] = 1
    return B

def countNeighbors(row, col, A):
    """
    Input: The coordinates of a point in a 2-D list biven using two integers and the list
    Ouptu: The number of living cells that are neighbors to the one at the given point
    """
    return A[row - 1][col - 1] + A[row - 1][col] + A[row - 1][col + 1] + A[row][col - 1] + A[row][col + 1] + A[row + 1][col - 1] + A[row + 1][col] + A[row + 1][col + 1]
