"""
Given an array of integers. All numbers occur twice except one number which occurs once. Find the number in O(n) time & constant extra space.
"""

def find_single_number(arr, n):
    result = arr[0]
    for i in range(1, n):
        result = result ^ arr[i]
    return result


if __name__ == "__main__":
    a = [2, 3, 5, 4, 5, 3, 4]
    print(find_single_number(a, len(a)))
