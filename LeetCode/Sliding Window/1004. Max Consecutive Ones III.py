class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        best = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # shrink while we have more than k zeros in window
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # window [left..right] is valid now
            best = max(best, right - left + 1)

        return best
        
        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1