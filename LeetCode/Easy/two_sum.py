"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
class Solution:
    def twoSum(self, nums, target):
        if not nums or len(nums) < 2:
            return []
        
        seen = {}
        for i in range(len(nums)):
            num_needed = target - nums[i]
            if num_needed in seen:
                return [i, seen[num_needed]]
            else:
                seen[nums[i]] = i
        return []
    

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 18
    print(Solution().twoSum(nums, target))