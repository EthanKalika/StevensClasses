def bibaLoop(lst):
    counter = 0
    for i in range(len(lst)):
        e = lst[i]
        if e == 'A':
            counter = counter + 5
        elif e == 'B':
            counter *= 2
        elif e == 'C':
            counter += adder(counter)
        elif e == 'D':
                counter = biba1(lst, i - 3, counter)
        elif e == 'E':
            counter -= 13
            counter += 5
            counter *= 2
            counter += 5
        elif e == 'F':
            counter = len(str(counter))
        print(counter)
    return counter

def biba1(lst, i, counter):
    e = lst[i]
    print(e)
    if e == 'A':
        counter = counter + 5
    elif e == 'B':
        counter *= 2
    elif e == 'C':
        counter += adder(counter)
    elif e == 'D':
        biba2(lst, i - 3, counter)
    elif e == 'E':
        counter -= 13
        counter += 5
        counter *= 2
        counter += 5
    elif e == 'F':
        counter = len(str(counter))
    return counter
    

def biba2(lst, i, counter):
    e = lst[i]
    if e == 'A':
        counter = counter + 5
    elif e == 'B':
        counter *= 2
    elif e == 'C':
        counter += adder(counter)
    elif e == 'D':
        biba3(lst, i - 3, counter)
    elif e == 'E':
        counter -= 13
        counter += 5
        counter *= 2
        counter += 5
    elif e == 'F':
        counter = len(str(counter))
    return counter

def biba3(lst, i, counter):
    e = lst[i]
    if e == 'A':
        counter = counter + 5
    elif e == 'B':
        counter *= 2
    elif e == 'C':
        counter += adder(counter)
    elif e == 'D':
        biba4(lst, i - 3, counter)
    elif e == 'E':
        counter -= 13
        counter += 5
        counter *= 2
        counter += 5
    elif e == 'F':
        counter = len(str(counter))
    return counter

def biba4(lst, i, counter):
    e = lst[i]
    if e == 'A':
        counter = counter + 5
    elif e == 'B':
        counter *= 2
    elif e == 'C':
        counter += adder(counter)
    elif e == 'E':
        counter -= 13
        counter += 5
        counter *= 2
        counter += 5
    elif e == 'F':
        counter = len(str(counter))
    return counter

def adder(num):
    if num < 10:
        return num
    else:
        return num % 10 + adder(num // 10)
'''
def bibaLoopRec(lst, a = 0, lstSub == []):
    if lst == []:
        return a
    if lst[3] == 'D':
        lstSub += lst[0]
    if lst[0] == 'A':
        bibaLoopRec(lst[1:], a = a + 5, lstSub)
    elif lst[0] == 'B':
        bibaLoopRec(lst[1:], a = a * 2, lstSub)
    elif lst[0] == 'C':
        bibaLoopRec(lst[1:], a = adder(a), lstSub)
    elif lst[0] == 'D':
        bibaLoopRec(lstSub[0] + lst[1:], lstSub[1:])
    elif lst[0] == 'E':
        bibaLoopRec(lst[1:], a = ((a - 8) * 2) = 5, lstSub)
'''
        
def bibaLoopRec(lst, a = 0, i = 0):
    if i > len(lst) - 1:
        return a
    if lst[i] == 'A':
        i += 1
        bibaLoopRec(lst, a + 5, i)
    elif lst[i] == 'B':
        i += 1
        bibaLoopRec(lst, a * 2, i)
    elif lst[i] == 'C':
        i += 1
        bibaLoopRec(lst, adder(a), i)
    elif lst[i] == 'D':
        bibaLoopRec(lst, a, i - 3)
        i += 1
    elif lst[i] == 'E':
        i += 1
        bibaLoopRec(lst, ((a - 8) * 2) + 5, i)
    elif lst[i] == 'F':
        i += 1
        bibaLoopRec(lst, len(str(a)), i)
