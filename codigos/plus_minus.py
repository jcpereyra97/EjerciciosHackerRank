import math
import os
import random
import re
import sys

"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and 
zero. Print the decimal value of each fraction on a new line with  places after the decimal.
"""



def plusMinus(arr):
    pos = 0.0
    neg = 0.0
    zero = 0.0
    tam = len(arr)
    for i in arr:
        if(i > 0):
            pos = pos + 1.0
        elif(i<0):
            neg = neg + 1.0
        else:
            zero = zero +1
    return print(str((pos/tam))+'\n'+str((neg/tam))+'\n'+str((zero/tam)))



plusMinus([-4, 3, -9, 0, 4, 1])
