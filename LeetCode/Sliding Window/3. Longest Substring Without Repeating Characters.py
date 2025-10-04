class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        res = 0
        i = 0
        for j, ch in enumerate(s):
            if ch in last:
                i = max(i, last[ch])
            res = max(res, j - i + 1)
            last[ch] = j + 1
        return res