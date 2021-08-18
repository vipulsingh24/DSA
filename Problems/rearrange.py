def rearrange(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1

    return arr

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print(rearrange(arr))


# Time - O(N)
# Space - O(1)
