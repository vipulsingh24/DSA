def rearrange_numbers_2(nums):
    if not nums:
        return []
    
    nums_freq = {}
    for num in nums:
        nums_freq[num] = nums_freq.get(num, 0) + 1
        
    results = [0] * len(nums_freq)
    
    for idx, item in enumerate(nums_freq):
        results[idx] = [item, nums_freq[item]]
        
    results = sorted(results, key=lambda x: x[1], reverse=True)
    results = sorted(results, key=lambda x: x[0], reverse=True)
    
    temp = []
    for i in range(len(results)):
        temp.append(results[i][0])
        
    return temp


arr =  [9,7,9, 5,3,7,5,7]
print(rearrange_numbers_2(arr))

arr =  [1,2,3,4,5,6,7]
print(rearrange_numbers_2(arr))

arr =  []
print(rearrange_numbers_2(arr))

arr =  [1,2,2,3,3,3]
print(rearrange_numbers_2(arr))

arr =  [1,2,2,2,3,3,3]
print(rearrange_numbers_2(arr))


"""
Output:
[9, 7, 5, 3]
[7, 6, 5, 4, 3, 2, 1]
[]
[3, 2, 1]
[3, 2, 1]
"""
