"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum(nums, target):
    if not nums or len(nums) < 2:
        return []

    seen = {}
    for i in range(len(nums)):
        num_needed = target - nums[i]
        if num_needed in seen:
            return [i, seen[num_needed]]
        else:
            seen[nums[i]] = i

