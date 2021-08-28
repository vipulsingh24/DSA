"""
Largest K such that both K and -K exist in array
"""


def largest_num(arr):
    left = 0
    right = len(arr) - 1

    arr = sorted(arr)
    
    while (left < right):
        sum = arr[left] + arr[right]
        if sum == 0:
            return arr[right]
        elif sum < 0:
            left += 1
        else:
            right -= 1

    return 0


def largest_num_set(arr):
    result = 0
    nums_set = set()
    for i in range(len(arr)):
        nums_set.add(-1 * arr[i])

        if (arr[i] in nums_set):
            result = max(result, abs(arr[i]))

    return result


if __name__ == "__main__":
    print(largest_num([3, 2, -2, 5, -3]))
    print(largest_num([3, 2, -2, -4, 5, 4, -3]))
    print(largest_num_set([3, 2, -2, 5, -3]))
    print(largest_num_set([3, 2, -2, -4, 5, 4, -3]))
