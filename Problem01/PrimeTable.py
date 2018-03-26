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
size = size + 1

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

while Prime[idxA] <= math.ceil(paraA):
    testFactor = paraA % Prime[idxA]
    if testFactor == 0:
        factorA.append(Prime[idxA])
    else:
        pass
    idxA = idxA + 1

print(factorA)

# exclude the prime factor of given number A
AllNumber = np.ones(size)
AllNumber[0] = 0

for i in range(0, len(factorA)):
    AddStep = factorA[i]
    NowValue = AddStep
    while NowValue < size:
        AllNumber[NowValue] = 0
        NowValue = NowValue + AddStep

prob = np.sum(AllNumber) / (AllNumber.shape[0] - 1)
print('The probability of gcd(' + str(paraA) +  ', N) = 1 is ', prob)

