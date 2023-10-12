# Ethan Kalika
# "I pledge my honor that I ahve abided by the Stevens Honor System"

from math import sqrt

class QuadraticEquation:

    def __init__(self, a, b, c):
        '''
        Input: self, and three floats a, b, and c
        Action: Creates a quadratic equation object with the given parameters
        '''
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def getA(self):
        '''
        Input: self
        Output: self's a value
        '''
        return self.a

    def getB(self):
        '''
        Input: self
        Output: self's b value
        '''
        return self.b

    def getC(self):
        '''
        Input: self
        Output: self's c value
        '''
        return self.c

    def discriminant(self):
        '''
        Input: self
        Output: self's descriminant
        '''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        return b ** 2 - 4 * a * c

    def root1(self):
        '''
        Input: self
        Output: self's first root
        '''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        disc = self.discriminant()
        if disc < 0:
            return None
        return (-1 * b + sqrt(disc)) / (2 * a)

    def root2(self):
        '''
        Input: self
        Output: self's second root
        '''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        disc = self.discriminant()
        if disc < 0:
            return None
        return (-1 * b - sqrt(disc)) / (2 * a)

    def __str__(self):
        '''
        Input: self
        Output: self's string representation
        '''
        parta = ''
        partb = ''
        partc = ''
        a = self.getA()
        b = self.getB()
        c = self.getC()
        if a == 1:
            parta += 'x^2'
        elif a == -1:
            parta += '-x^2'
        else:
            parta += str(a) + 'x^2'
        if b == 1:
            partb += ' + x'
        elif b == -1:
            partb += ' - x'
        elif b > 0:
            partb += ' + ' + str(b) +'x'
        elif b < 0:
            partb += ' ' + str(b)[0] + ' ' + str(b)[1:] + 'x'
        if c == 1:
            partc += ' + 1.0'
        elif c == -1:
            partc += ' - 1.0'
        elif c > 0:
            partc += ' + ' + str(c)
        elif c < 0:
            partc += ' ' + str(c)[0] + ' ' + str(c)[1:]
        return parta + partb + partc + ' = 0'
