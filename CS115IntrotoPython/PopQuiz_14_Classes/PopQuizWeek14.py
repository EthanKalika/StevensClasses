# Ethan Kalika
# "I pledge my honor that I have abided by the Stevens Honor System"

class Student:
    def __init__(self, first, last):
        self.name = first
        self.surname = last
        self.grades = []

    def getFirstName(self):
        return self.name
        
    def getLastName(self):
        return slef.surname
        
    def setFirstName(self, newName):
        self.name = newName
        
    def setLastName(self, newSurname):
        self.surname = newSurname
        
    def addGrade(self, newGrade):
        self.grades += [newGrade]
        
    def computeGPA(self):
        allGrades = sum(self.grades)
        return allGrades / len(self.grades)
    def __str__(self):
        return self.name + " " + self.surname + " has a GPA of "+str(self.computeGPA())

s1 = Student("Maria", "Doe")
s1.addGrade(100)
s1.addGrade(80)
s1.addGrade(90)
s1.setFirstName("John")
print(s1)
