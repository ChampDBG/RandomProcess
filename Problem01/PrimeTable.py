# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:47:45 2018

@author: WU

This funciton is used to create the prime table
"""
# import math
import numpy as np

size = 100

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
print(Prime)