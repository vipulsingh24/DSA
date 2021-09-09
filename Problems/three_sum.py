"""
Find all unique triplets in the array which gives the sum of zero

nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1,-1,2], [-1,0,1]]
"""


def three_sum(nums):
    if not nums or len(nums) < 0:
        return []

    result = []
    nums.sort()  # [-4, -1, -1, -1, 0, 1, 2]

    for idx in range(len(nums)):  # idx = 0
        left = idx + 1  # 1
        right = len(nums) - 1  # 6
        if idx > 0 and nums[idx] == nums[idx-1]:  # idx = 0
            continue

        while left < right:  # 1<6, 2<6
            total = nums[idx] + nums[left] + nums[right]  # -4+-1+2=-3 => -4-1+2=-3 => -4
            if total == 0:
                result.append([nums[idx], nums[left], nums[right])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left+1]:
                    left += 1
  
                while left < right and nums[right] == nums[right+1]:
                    right += 1
            elif total < 0:  # total=-3 => -3
                left += 1  # left = 2, 3
            else:
                right -= 1

    return result

        
