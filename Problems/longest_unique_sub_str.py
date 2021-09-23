

def longest_unique_sub_str(strr):
    n = len(strr)
    last_idx = {}
    max_len = 0
    start_idx = 0

    for i in range(n):
        if strr[i] in last_idx:
            start_idx = max(start_idx, last_idx[strr[i]] + 1)

        max_len = max(max_len, i - start_idx + 1)
        last_idx[strr[i]] = i

    return max_len


s = "abcabcd"
print(longest_unique_sub_str(s))
