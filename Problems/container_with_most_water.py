
# Python3 code for Max
# Water Container
def maxArea(A, Len) :
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           
            # Calculating the max area
            area = max(area, min(A[j], A[i]) * (j - i))
    return area
 
# Driver code
a = [ 1, 5, 4, 3 ]
b = [ 3, 1, 2, 4, 5 ]
 
len1 = len(a)
print(maxArea(a, len1))
 
len2 = len(b)
print(maxArea(b, len2))

Time Complexity: O(n^2). 
As nested traversal of the array is required, so time complexity is O(n^2)
Space Complexity: O(1). 


# Python3 code for Max
# Water Container
def maxArea( A):
    l = 0
    r = len(A) -1
    area = 0
     
    while l < r:
        # Calculating the max area
        area = max(area, min(A[l],
                        A[r]) * (r - l))
     
        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area
 
# Driver code
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]

print(maxArea(a))
print(maxArea(b))

Time Complexity: O(n). 
As only one traversal of the array is required, so time complexity is O(n).
Space Complexity: O(1). 
