'''
Created on Jan 20, 2015

@author: Brian Borowski

CS115 - Lab 1 Test Script
'''
import unittest
import lab1 #change lab1Solution with the name of your solution file

class Test(unittest.TestCase):

    def testInverse1(self):
        self.assertAlmostEqual(lab1.inverse(1), 1, 6)

    def testInverse2(self):
        self.assertAlmostEqual(lab1.inverse(2), 0.5, 6)

    def testInverse3(self):
        self.assertAlmostEqual(lab1.inverse(3), 0.3333333333333333, 6)

    def testInverse4(self):
        self.assertAlmostEqual(lab1.inverse(-3), -0.3333333333333333, 6)

    def testE1(self):
        self.assertAlmostEqual(lab1.e(1), 2, 6)

    def testE2(self):
        self.assertAlmostEqual(lab1.e(2), 2.5, 6)

    def testE3(self):
        self.assertAlmostEqual(lab1.e(10), 2.718281801146385, 10)

    def testE4(self):
        self.assertAlmostEqual(lab1.e(100), 2.7182818284590455, 10)


if __name__ == "__main__":
    unittest.main()
