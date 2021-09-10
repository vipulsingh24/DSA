"""
Given an array of size n that has the following specifications: 

Each element in the array contains either a policeman or a thief.
Each policeman can catch only one thief.
A policeman cannot catch a thief who is more than K units away from the policeman.
We need to find the maximum number of thieves that can be caught.


Input : arr[] = {'P', 'T', 'T', 'P', 'T'},   k = 1.
Output : 2.
"""


def max_number_thief_caught(arr, k):
    n = len(arr)
    i = 0
    t = 0
    p = 0
    result = 0
    theif = []  # [1,2,4]  # [0,1,4]
    police = []  # [0,3]   # [2,3,5]s

    while i < n:
        if arr[i] == "P":
            police.append(i)
        elif arr[i] == "T":
            theif.append(i)
        i += 1

    while t < len(theif) and p < len(police):
        if abs(theif[t] - police[p]) <= k:
            result += 1
            t += 1
            p += 1
        elif theif[t] < police[p]:
            t += 1
        else:
            p += 1

    return result

if __name__=='__main__':
    arr1 = ['P', 'T', 'T', 'P', 'T']
    k = 2
    print(("Maximum thieves caught: {}".format(max_number_thief_caught(arr1, k))))
 
    arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
    k = 2
    print(("Maximum thieves caught: {}".format(max_number_thief_caught(arr2, k))))
