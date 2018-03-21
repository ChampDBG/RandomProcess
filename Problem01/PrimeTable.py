# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:47:45 2018

@author: WU

This funciton is used to create the prime table
"""
import math
import numpy as np

# set the range of total numbers
size = input("The Size of potential random number: ")
size = int(size)

# setup the prime table of the range
PrimeTable = np.ones(size)
PrimeTable[0] = 0
PrimeTable[1] = 0

for i in range(0, size):
    if PrimeTable[i]:
        for j in range(i+i, size, i):
            PrimeTable[j] = 0
    else:
        pass

Prime = np.where(PrimeTable)
Prime = list(Prime[0])

# set the given number and divide with prime factor
paraA = input("The given number is: ")
paraA = int(paraA)

factorA = []
idxA = 0

while Prime[idxA] < int(math.ceil(paraA/2.0)):
    testFactor = paraA % Prime[idxA]
    if testFactor == 0:
        factorA.append(Prime[idxA])
    else:
        pass
    idxA = idxA + 1

# inclusion-exclusion 
