class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left, res, max_count = 0, 0, 0

        for right, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            count[idx] += 1
            if count[idx] > max_count:
                max_count = count[idx]
            
            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left +=1
            
            res = max(res, right - left + 1)
        
        return res