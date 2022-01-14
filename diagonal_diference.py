import math
import os
import random
import re
import sys

"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""


def diagonal(arr):
    der = 0
    izq = 0
    j = len(arr[0]) - 1
    for i in range(0,len(arr)):
        der = der +(arr[i][i])
        izq = izq + (arr[i][j])
        j = j - 1
    return abs((izq) - (der))
    
print(diagonal([[11,2,4],[4,5,6],[10,8,-12]]))
