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
    low = 0
    high = len(lst) - 1
    first = 0
    last = 0
    while high >= low:
        mid = (low + high) // 2
        if lst[mid] == key and !(lst[mid - 1] == key):
            
        else:
            if lst[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
    return num
