class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        # frequency arrays for lowercase letters
        need = [0] * 26
        win  = [0] * 26
        base = ord('a')

        for ch in s1:
            need[ord(ch) - base] += 1

        # initialize first window
        for i in range(m):
            win[ord(s2[i]) - base] += 1

        if win == need:
            return True

        # slide window over s2
        for i in range(m, n):
            # add s2[i], remove s2[i-m]
            win[ord(s2[i]) - base] += 1
            win[ord(s2[i - m]) - base] -= 1
            if win == need:
                return True

        return False