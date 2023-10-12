#!/usr/bin/env python
# coding: utf-8

# In[1]:


grades = {
    "John": [98, 79, 100],
    "Mary": [56, 79, 28],
    "Eve": [68, 45, 88],
    "Alice": [80, 99, 65],
    "Bob": [87, 90, 95]
}

def listStudents(dic):
    """Given a dictionary with (student name,list of grades) as key-value pairs, 
       return the list of students names"""
    return list(dic.keys())

#Write a lambda function that takes a list as an input and returns the mean of the lists elements
list_average = lambda x: sum(x) / len(x)


def searchStudent(dic, name):
    """Given a dictionary with (student name,list of grades) as key-value pairs and a student name,
       return a tuple containing the student name and average grade for that student"""
    if (name in dic):
        return (name, list_average(dic[name]))
    else:
        return "student not found"


def computeIndividualAverage(grades):
    """Given a dictionary with (student name,list of grades) as key-value pairs,
       return a dictionary containing the student name and average grade as key-value pairs"""
    return dict(map(lambda dict_item: (dict_item[0], list_average(dict_item[1])), grades.items()))

def getSubsetStudents(grades, threshold):
    """Given a dictionary with (student name,list of grades) as key-value pairs and a threshold,
       return a list of tuples containing the names and the average grades of students with average grade greater than the threshold"""
    return list(filter(lambda x: x[1] >= threshold, computeIndividualAverage(grades).items()))
