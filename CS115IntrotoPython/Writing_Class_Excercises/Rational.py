class Rational:

    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d


    def isZero(self):
        return self.numerator == 0
    

    def add(self, other):
        newNumerator = self.numerator * other.denominator +\
                       self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)


    def __add__(self, other):
        newNumerator = self.numerator * other.denominator +\
                       self.denominator * other.numerator
        newDenominator = self.denominator * other. denominator
        return Rational(newNumerator, newDenominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


