class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k % n
        nums = self.reverse(nums, 0, n - 1)
        nums = self.reverse(nums, 0, k - 1)
        nums = self.reverse(nums, k, n - 1)
        return nums
    
    def reverse(self, nums, start, end):
        while start <= end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums
