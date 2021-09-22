#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

def longestChain(words):
    # Write your code here
    if not words:
        return 0
    
    if len(words) == 1:
        return 1
    
    words = sorted(words, key=lambda x: len(x))
    ref = {word: 1 for word in words}
    
    for word in words:
        for index in range(len(word)):
            new_word = word[:index] + word[index+1:]
            if new_word in ref:
                ref[word] = max(ref[word], ref[new_word] + 1)
        
        if word not in ref:
            ref[word] = 1
            
    result = sorted(ref.items(), key=lambda x: x[1], reverse=True)
    return result[0][1]


if __name__ == '__main__':
