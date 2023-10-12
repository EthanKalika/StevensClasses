# Ethan Kalika
# "I pledge my honor that I have abided by the Stevens Honor System"

def pascal_row(n):
    """
    Input: A nonegative integer
    Output: That integer row of the pascal triangle
    """
    if n == 0:
        return [1]
    else:
        return [1] + crumple(pascal_row(n - 1)) + [1]

def crumple(L):
    """
    Input: A list
    Output: A new list where each element is the sum of adjacent elements in the given one
    """
    if len(L) == 1:
        return []
    else:
        return [L[0] + L[1]] + crumple(L[1:])
    
def pascal_triangle(n):
    """
    Input: A positive integer
    Output: All rows of the pascal trianlge up to and including that of the given integer
    """
    if n == 0:
        return [[1]]
    else:
        return pascal_triangle(n - 1) + [pascal_row(n)]

def test_pascal_row():
    # Tests if the pascal_row function works properly
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(6) == [1, 6, 15, 20, 15, 6, 1]

def test_pascal_triangle():
    # Tests if the pascal_triangle function works properly
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
