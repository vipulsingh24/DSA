"""
Sign of the Product of an Array
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
"""


class Solution(object):
    
    def arraySign(self, nums):
        negatives_count = 0
        for num in nums:
            if num == 0:
                return 0
            
            if num < 0:
                negatives_count += 1
        
        return 1 if negatives_count % 2 == 0 else -1
    
      #         product = 1
#         for num in nums:
#             if num == 0:
#                 return 0
#             product *= num
        
#         return -1 if product < 0 else 1
    
    
#     def signProduct(self, num):
#         if num > 0:
#             return 1
#         elif num < 0:
#             return -1
#         elif num == 0:
#             return 0
        
#     def arraySign(self, nums):
#         product = functools.reduce(lambda a, b: a * b, nums)
#         return self.signProduct(product)
    
#     def arraySign(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         zeroes, negatives = 0, 0
#         for num in nums:
#             if num == 0:
#                 zeroes += 1
            
#             if num < 0:
#                 negatives += 1
                
#         if zeroes > 0:
#             return 0
#         elif negatives % 2 == 0:
#             return 1
#         else:
#             return -1
            
