"""
An alternate sort of list consists of alternate elements starting from the first position of the given list after sorting it in ascending order. You are given a list of unsorted elements. Write an algorithm to find the alternate sort of the given list. Python program 

Example 
Input: 3 5 1 5 9 10 2 6
Output: 1 3 5 9
"""

def alternate_sort(arr):
    arr.sort()
    return arr[::2]

input = [3,5,1,5,9,10,2,6]
print(alternate_sort(input))