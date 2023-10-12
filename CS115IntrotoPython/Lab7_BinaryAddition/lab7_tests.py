from lab7 import *

assert gor3(0,0,0) == 0
assert gor3(0,0,1) == 1
assert gor3(0,1,0) == 1
assert gor3(0,1,1) == 1
assert gor3(1,0,0) == 1 
assert gor3(1,0,1) == 1 
assert gor3(1,1,0) == 1 
assert gor3(1,1,1) == 1 

assert FA(0,0,0) == (0,0)
assert FA(0,0,1) == (0,1)
assert FA(0,1,0) == (0,1)
assert FA(0,1,1) == (1,0)
assert FA(1,0,0) == (0,1)
assert FA(1,0,1) == (1,0)
assert FA(1,1,0) == (1,0)
assert FA(1,1,1) == (1,1)

assert fourBitAdd((0,0,0,0), (0,0,0,0)) == (0, (0,0,0,0))
assert fourBitAdd((0,0,0,1), (0,0,0,0)) == (0, (0,0,0,1))
assert fourBitAdd((0,0,1,0), (0,0,0,0)) == (0, (0,0,1,0))
assert fourBitAdd((0,0,1,1), (0,0,0,0)) == (0, (0,0,1,1))
assert fourBitAdd((1,0,1,0), (1,0,1,0)) == (1, (0,1,0,0))
assert fourBitAdd((1,1,1,0), (1,1,1,0)) == (1, (1,1,0,0))
assert fourBitAdd((1,0,1,1), (0,1,0,1)) == (1, (0,0,0,0))
assert fourBitAdd((0,0,1,0), (0,0,0,1)) == (0, (0,0,1,1))
assert fourBitAdd((1,1,1,1), (0,1,1,0)) == (1, (0,1,0,1))