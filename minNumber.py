"""The first function should compare each number to every other number on the list O(n^2)
    The second function should be linear O(n)"""

test1 = [5,4,2,1,0]
test2 = [0,4,2,1,5]
import time
from random import randrange

def findMin1(lon): #Quadratic
    min = lon[0] #1
    for i in lon: #n
        issmallest = True
        for j in lon: #n
            if i > j:
                issmallest = False
        if issmallest:
            min = i
    return min

#print(findMin1(test1))  
#print(findMin1(test2))  

"""Test cases"""
"""for listSize in range(1000,10001,1000):
    lon = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin1(lon))
    end = time.time()
    print('size: %d time: %f' %(listSize,end-start))"""

def findMin2(lon): #linear
    minSoFar = lon[0] # 1
    for i in lon: # n
        if i < minSoFar:
            minSoFar = i
    return minSoFar

"""Test cases"""
for listSize in range(1000,10001,1000):
    lon = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin2(lon))
    end = time.time()
    print('size: %d time: %f' %(listSize,end-start))