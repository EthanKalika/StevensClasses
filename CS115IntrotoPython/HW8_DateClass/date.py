'''
Created on 4 / 27 / 22
@author:   Ethan Kalika
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
daysDict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self): 
        '''Returns a new object with the same month, day, year 
           as the calling object (self).''' 
        dnew = Date(self.month, self.day, self.year) 
        return dnew
    
    def equals(self, d2): 
        '''Decides if self and d2 represent the same calendar date, 
            whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        '''
        Input: A date object
        Action: Changes date to tomorrows date
        '''
        if self.month == 12 and self.day == 31:
            self.day = 1
            self.month = 1
            self.year += 1
        elif (self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10) and self.day == 31:
            self.day = 1
            self.month += 1
        elif (self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11) and self.day == 30:
            self.day = 1
            self.month += 1
        elif self.month == 2 and self.day == 28 and self.isLeapYear():
            self.day += 1
        elif self.month == 2 and self.day == 28:
            self.day = 1
            self.month += 1
        elif self.month == 2 and self.isLeapYear() and self.day == 29:
            self.day = 1
            self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        '''
        Input: A date object
        Action: Changes date to yesterdays date
        '''
        if self.isLeapYear() and self.month == 3 and self.day == 1:
            self.day = 29
            self.month -= 1
        elif self.month == 3 and self.day == 1:
            self.month = 2
            self.day = 28
        elif self.month == 1 and self.day == 1:
            self.day = 31
            self.month = 12
            self.year -= 1
        elif (self.month == 2 or self.month == 4 or self.month == 6 or self.month == 8 or self.month == 9 or self.month == 11) and self.day == 1:
            self.day = 31
            self.month -= 1
        elif (self.month == 3 or self.month == 5 or self.month == 7 or self.month == 10 or self.month == 12) and self.day == 1:
            self.day = 30
            self.month -= 1
        else:
            self.day -= 1

    def addNDays(self, N):
        '''
        Input: A date object and an integer (N)
        Action: Changes date to N days in the future and print all the dates
        '''
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        '''
        Input: A date object and an integer(N)
        Action: Changes date to N days in the past and print all the dates
        '''
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def isBefore(self, d2):
        '''
        Input: 2 date objects
        Ouput: A boolean that is true if and only if self is before d2
        '''
        if d2.year > self.year:
            return True
        elif d2.year < self.year:
            return False
        else:
            if d2.month > self.month:
                return True
            elif d2.month < self.month:
                return False
            else:
                if d2.day > self.day:
                    return True
                elif d2.day < self.day:
                    return False
        return False

    def isAfter(self, d2):
        '''
        Input: 2 date objects
        Ouput: A boolean that is true if and only if self is after d2
        '''
        if self.equals(d2):
            return False
        return not(self.isBefore(d2))

    def diff(self, d2):
        '''
        Input: 2 date objects
        Ouput: An integer representing the numebr of days between self and d2
        '''
        counter = 0
        otherDay = self.copy()
        while otherDay.isBefore(d2):
            counter -= 1
            #print(otherDay)
            otherDay.tomorrow()
        while otherDay.isAfter(d2):
            counter += 1
            #print(otherDay)
            otherDay.yesterday()
        return counter

    def dow(self):
        '''
        Input: A date object
        Ouput: The day of the week when that day took place
        '''
        num = (3 + self.diff(Date(11, 9, 2011))) % 7
        return daysDict[num]
