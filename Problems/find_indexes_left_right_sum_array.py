def find_parity_indexes(arr):
    n = len(arr)
    
    right_sum, left_sum = 0, 0
    
    for i in range(1, n):
        right_sum += arr[i]
        
    i = 0
    j = 1
    
    # Checking the point of partition
    indexes = []
    while j < n:
        right_sum -= arr[j]
        left_sum += arr[i]
        
        if right_sum == left_sum:
            indexes.append(i + 1)
        
        i += 1
        j += 1
    
    return indexes

a = [-23, 100, 0, 4, 34, 43]
print(find_parity_indexes(a))

a = [-7, 1, 5, 2, -4, 3, 0, 0]
print(find_parity_indexes(a))
