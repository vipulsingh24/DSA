"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output: 6  (j = 7, i = 1)
"""


def max_distance(arr):
    n = len(arr)
    
    l_min = [0] * n
    r_max = [0] * n

    l_min[0] = arr[0]  # [34]
    for i in range(1, n):
        l_min[i] = min(l_min[i -1], arr[i])  # [9, 2, 2, 2, 2, 2, 2, 2, 2, 0]

    r_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        r_max[i] = max(r_max[i+1], arr[i])  # [18, 18, 18, 18, 18, 18, 18, 18, 18, 0]
    
    i, j = 0, 0
    max_dis = -1

    while (j < n and i < n):
        if l_min[i] <= r_max[j]:
            max_dis = max(max_dis, j - i)
            j += 1
        else:
            i += 1

    return max_dis


if __name__ == "__main__":
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    print (max_distance(arr))  # 8
