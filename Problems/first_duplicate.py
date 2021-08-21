"""
value in list should be in range 1 - N (length of array)

[0,1,2,3,4,5] -> Invalid 
[1,2,3,1] -> 1
[1,3,2,3,4,5] -> 3
"""


"""
def first_duplicate(arr):
    min_second_idx = len(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                min_second_idx = min(min_second_idx, j)

    if min_second_idx == len(arr):
        return -1
    return arr[min_second_idx]
# Time Complexity : O(n^2)
"""


"""
def first_duplicate(arr):
    arr_set = set()
    for i in range(len(arr)):
        if arr[i] in arr_set:
            return arr[i]
        arr_set.add(arr[i])
    return -1

#Time Complexity : O(n)
#Space: O(n)
"""

def first_duplicate(arr):
    """
    Time Complexity : O(n)
    """
    for i in range(len(arr)):
        print("i: ", i)
        if (arr[abs(arr[i]) - 1] < 0):
            return abs(arr[i])
        else:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    return -1


if __name__ == "__main__":
    a = [1,3,2,3,4,5]
    print(first_duplicate(a))



