def max_min(arr, low, high):
    arr_max = arr[low]
    arr_min = arr[low]

    if low == high:
        return (arr_max, arr_min)
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
        mid = int((low + high) // 2)
        arr_max_1, arr_min_1 = max_min(arr, low, mid)
        arr_max_2, arr_min_2 = max_min(arr, mid+1, high)

    return (max(arr_max_1, arr_max_2), min(arr_min_1, arr_min_2))

arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = max_min(arr, low, high)
print("Array: ", arr)
print('Minimum element is ', arr_min)
print('\nMaximum element is ', arr_max)
