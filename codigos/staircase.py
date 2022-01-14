import math
import os
import random
import re
import sys

"""
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line 
is not preceded by any spaces.

Write a program that prints a staircase of size .
"""

def staircase(n):
    space = ' '
    ast = '#'
    j = (n - 1)
    for i in range(1,n+1):
        print(str(j*space)+str(i*ast)+'\n')
        j = j - 1

staircase(6)

