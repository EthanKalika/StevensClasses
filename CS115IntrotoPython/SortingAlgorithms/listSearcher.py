def fastSearch(lst, key):
    '''Searches the list for the key. If the key is present, the function retrurns th eindex of the key. Otherwise, it returns -1.'''
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

# This does not work
'''
def fasterSearch(sortedLst, key):
    i = len(sortedLst) // 2
    item = sortedLst[i]
    if item == sortedLst[i]:
        return i
    while item != key:
        if item > key:
            i = i // 2
        elif item < key:
            i = (i + len(sortedLst)) // 2
        elif sortedLst[i] == key:
            return i
        item = sortedLst[i]
'''

def binary_search(lst, key):
    '''
    Input: A sorted list and a key
    Output: The index of key in the lst
    '''
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        else:
            if lst[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
    return -1

def searchAll(lst, key):
    '''
    Input: A sorted list and a key
    Output: The number of times that the key appeard in the list
    '''
    low = 0
    high = len(lst) - 1
    numL = 0
    numH = 0
    while high >= low:
        mid = (low + high) // 2
        if mid == 0:
            numL = 0
            break
        elif lst[mid] == key and lst[mid - 1] != key:
            numL = mid
            break
        else:
            if lst[mid] < key:
                low = mid + 1
            elif lst[mid] > key or lst[mid - 1] >= key:
                high = mid - 1
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if mid == len(lst) - 1:
            numH = len(lst) - 1
            break
        elif lst[mid] == key and lst[mid + 1] != key:
            numH = mid
            break
        else:
            if lst[mid] < key or lst[mid + 1] <= key:
                low = mid + 1
            elif lst[mid] > key:
                high = mid - 1
    if lst[numH] != key:
        return -1
    return numH - numL + 1

def slowSearch(lst, key):
    '''
    Input: A sorted list and a key
    Output: The number of times that the key appeard in the list
    '''
    count = 0
    for element in lst:
        if element == key:
            count += 1
    return count
