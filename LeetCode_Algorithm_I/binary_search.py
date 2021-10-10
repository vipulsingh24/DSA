"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        else:
            low = 0
            high = len(nums)-1
            counter = 0
            while low <= high:
                # mid = (low + high)//2
                mid = low + (high-low)//2
                if nums[mid] == target:
                    return mid      ## Success, Found
                elif nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                counter += 1
                if counter > len(nums):
                    break

            return -1       #
