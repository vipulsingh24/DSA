from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)            # required counts for each char in t
        window = defaultdict(int)    # counts for current window
        required = len(need)         # number of distinct chars we must satisfy
        formed = 0                   # how many distinct chars currently satisfied

        l = 0
        min_len = float('inf')
        min_l = 0

        # expand the window with r
        for r, ch in enumerate(s):
            window[ch] += 1
            # if this char now satisfies the required count, increment formed
            if window[ch] == need.get(ch, 0):
                formed += 1

            # contract window while it remains valid
            while l <= r and formed == required:
                # update minimum window
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_l = l

                # remove leftmost char and move left forward
                left_char = s[l]
                window[left_char] -= 1
                if window[left_char] < need.get(left_char, 0):
                    formed -= 1
                l += 1

        if min_len == float('inf'):
            return ""
        return s[min_l:min_l + min_len]