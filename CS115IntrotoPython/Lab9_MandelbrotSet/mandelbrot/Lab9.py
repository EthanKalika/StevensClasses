# mandelbrot.py
# Lab 9
#
# Name: Ethan Kalika
# "I pledge my honor that I have abided by the Stevens Honor System"

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

from cs5png import *

def mult(c, n):
    """
    Input: Two positive integer n and a real number c
    Output: Their product
    """
    result = 0
    for x in range(n):
        result += c
    return result

def update(c, n):
    """
    Input: A complex value c and a positive integer n
    Output: The nth itteration of z = z ** 2 + c
    """
    z = 0
    for i in range(n):
        z = z ** 2 + c
    return z

def inMSet(c, n):
    """
    Input: A complex number c and an integer n
    Output: A boolean that is true if and only if c is in the Mandelbrot set
    Notes:
        c is used for the update step of z = z ** 2 + c
        n is the maximum number of times to run the update step
        The function returns False as soon as abs(z) gets larger than 2
        The function returns True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for i in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True
        
def weWantThisPixel (col, row):
    """
    a function that returns True if we want the pixel at col, row and False otherwise
    """
    if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False

def test():
    """
    A function to demonstrate how to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw aome pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file

    image.saveFile()
    """
    If the line "if col % 10 == 0 and row % 10 == 0" was changed to "if col % 10 == 0 or row % 10 == 0" then instead of displaying a lattice of points the image will display a grid of perpendicular and
    parallel lines separated by 10 pixles
    """

def scale(pix, pixelMax, floatMin, floatMax):
    """
    Input: Integer, pix and pixelMax, and floats floatMin and floatMax
        pix, the CURRENT pixel column (or row)
        pixMax, the total number of pixel columns
        floatMin, the min floating_point value
        floatMax, the max floating_point value
    Output: A number between floatMin and floatMax corresponding to where pix is between 0 and pixelMax
        returns the floating point value corresponding to pix
    """
    return floatMin + float(pix / pixelMax) * (floatMax - floatMin)

def mset(width, height):
    """
    Input: Positive integers width and height
    Output: An image of the Mandelbrot set with dimensions width by height
    """

def mset():
    """
    Creates a 300 * 200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        x = scale(col, 300, -2.0, 1.0)
        for row in range(height):
            y = scale(row, 200, -1.0, 1.0)
            c = x + y * 1j
            if inMSet(c, 25):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file

    image.saveFile()
