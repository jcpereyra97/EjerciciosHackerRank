import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arreglo = sorted(arr)
    max = 0
    min = 0
    j = 4
    for i in range(0,4):
        max = max + (arreglo[j])
        min = min + (arreglo[i])
        j = j - 1
    return max,min

print(miniMaxSum([1,2,3,4,5]))
    

