def longest_substr_no_repeating_chars(self, s):
  size = len(s)
  last_seen = {}

  left, right, ans = 0, 0, 0

  while left <= right < size:
    char = s[right]
    if char in last_seen:
      left = max(last_seen.get(char)+1, left)

    last_seen[char] = right
    ans = max(ans, right - left + 1)
    right+=1 

  return ans


def longest_substr_no_repeating_chars_2(self, s):
  last_seen_index = {}
  max_len, curr, i = 0, 0, 0
  size = len(s)
  while i < size:
    char = s[i]
    if char in last_seen_index:
      max_len = max(max_len, curr)
      i = last_seen_index[char]
      last_seen_index = {}
      curr=0
    else:
      curr += 1
      last_seen_index[char] = i

      i += 1
  max_len = max(max_len, curr)       
  return max_len 
