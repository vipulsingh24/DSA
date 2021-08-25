"""
A peak element is an element that is greater than its neighbors

ip: [1,2,3,1]
op: 2 (3 is the element and its index is 2)
"""

def find_peak_element(arr):
    left = 0
    right = len(arr) - 1
 
    while (left < right):
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    a = [1,2,3,1]
    print(find_peak_element(a))
 
