class PointLine:
    def __init__(self, inputX, inputY):
        """ Assign inputX and input Y to the attributes x and y """
        self.xCoord = inputX
        self.yCoord = inputY
        
    def setXCoordinate(self, newX):
        """ Reset the value of the x-coodinate, if the new value of the x-coordinate
            is a decimal or integer. Print an error message otherwise.
        """
        # self.xCoord = newX (Person might not enter a float or int)
        if isinstance(newX, float) or isinstance(newX, int):
            self.xCoord = newX
        else:
            print("X-coordinate should be a decimal or integer")

    def setYCoordinate(self, newY):
        """ Reset the value of the y-coodinate, if the new value of the y-coordinate
            is a decimal or integer. Print an error message otherwise.
        """
        # self.yCoord = newY (Person might not enter a float or int)
        if isinstance(newY, float) or isinstance(newX, int):
            slef.yCoord = newY
        else:
            print("Y-coordinate should be a decimal or integer")

    def getXCoordinate(self):
        """ Return the x-coordinate of the point """
        return self.xCoord

    def getYCoordinate(self):
        """ Return the y-coordinate of the point """
        return self.yCoord

    def __repr__(self):
        """ Return a string representation of the point.
            For example for x = 2 and y = 3 we should get (2 , 3) back
        """
        return str(self)
    
    def __str__(self):
        """ Return a string representation of the point.
            For example for x = 2 and y = 3 we should get (2 , 3) back
        """
        return '(' + str(self.xCoord) + ' , ' + str(self.yCoord) + ')'

    def __eq__(self, other):
        """ Returns True if two points are equal and False otherwise """
        return self.xCoord == other.xCoord and self.yCoord == other.yCoord

    
class Line:
    def __init__(self, Point1, Point2):
        """ Declare and initialize the 4 attributes of the class Line:
            Point1, Point2, slope and y-intercept
        """
        '''
        if Point2.getXCoordinate() == Point1.getXCoordinate():
            raise ValueError("x-coordinates of points can't be the same, or else the line is vertical")
        else:
            self.Slope = (Point2.getYCoordinate() - Point1.getYCoordinate()) / (Point2.getXCoordinate() - Point1.getXCoordinate())
        self.YIntercept = Point1.getYCoordinate() - Point1.getXCoordinate() * self.Slope
        ''' # Points should also be attributes
        self.p1 = Point1
        self.p2 = Point2
        self.slope = (point2.getYCoordinate() - Point.getYCoordinate()) / (Point2.getXCoordinate() - Point1.getXCoordinate())
        self.yintercept = Point1.getYCoordinate() - Point1.getXCoordinate() * self.slope

    def getSlope(self):
        """ Return the slope of the line """
        return self.slope
    
    def getYIntercept(self):
        """ Return the y-intercept of the line """
        return self.Yintercept

    def __repr__(self):
        """ Return a string representation of the line.
            For example, if slope = 1 and y-intercept=1, we should get 'y= 1x + 1' back
        """
        return str(self)

    def __str__(self):
        """ Return a string representation of the line.
            For example, if slope = 1 and y-intercept=1, we should get 'y= 1x + 1' back
        """
        return 'y= ' + str(self.slope) + 'x + ' + str(self.Yintercept)

    def __eq__(self, other):
        """ Returns True if two lines are equal and False otherwise """
        return self.Slope == other.Slope and self.Yintercept == other.Yintercept
    
    def parallel(self, other):
        """ Returns True if two lines are parallel and False otherwise """
        return self.slope == other.slope

    def intersection(self, other):
        """ Returns the intersection point of two lines """
        xToReturn = (other.Yintercept - self.Yintercept) / (self.slope - other.slope)
        yToReturn = self.slope * xToReturn + self.Yintercept
        return __init__(xToReturn, yToReturn)
