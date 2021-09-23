class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trap = [0] * n
        result = 0
        
        l_max = [0] * n
        r_max = [0] * n
        
        l_max[0] = height[0]
        for j in range(1, n):
            l_max[j] = max(l_max[j-1], height[j])
            
        r_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])
            
        for i in range(n):
            result += min(l_max[i], r_max[i]) - height[i]
            
        return result
