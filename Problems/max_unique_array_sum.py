#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumUniqueSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinimumUniqueSum(arr):
    # Write your code here
    n = len(arr)
    
    arr = sorted(arr)
    
    sum = arr[0]  # 3
    previous = arr[0]  #  
    
    for i in range(1, n):
        current_element = arr[i] # 2
        
        if current_element <= previous:
            previous += 1
            sum += previous
        else:
            sum += current_element
            previous = current_element
        
    return sum
