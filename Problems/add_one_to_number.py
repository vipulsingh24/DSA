"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
"""

def add_one_to_numbers(nums):
    n = len(nums)

    nums[n-1] += 1
    carry = nums[n-1] / 10
    nums[n-1] = nums[n-1] % 10

    for i in range(n-2, -1, -1):
        if carry == 1:
            nums[i] += 1
            carry = nums[i] / 10
            nums[i] = nums[i] % 10

    if carry == 1:
        nums.insert(0, 1)

    return nums


if __name__ == "__main__":
    a = [1,7,8,9]
    print(add_one_to_numbers(a))
