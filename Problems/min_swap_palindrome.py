"""
Min Adj Swaps to Make Palindrome
"""

def is_palindrome_possible(s):
    char_count = [0] * 26

    for char in s:        
        char_count[ord(char) - ord('a')] += 1

    odd_count = 0
    for i in char_count:
        if i % 2 != 0 and i > 0:
            odd_count += 1

    return odd_count <= 1 

def min_swap_palindrome(s):
    if not s:
        return -1

    swap_count = 0

    if is_palindrome_possible(s):
        left_idx = 0
        right_idx = len(s) - 1
        s = list(s)

        while (left_idx < right_idx):
            if s[left_idx] == s[right_idx]:
                left_idx += 1
                right_idx -= 1
            else:
                temp_right_idx = right_idx
                
                while (left_idx < temp_right_idx and s[left_idx] != s[temp_right_idx]):
                    temp_right_idx -= 1

                if (left_idx == temp_right_idx):
                    (s[left_idx], s[left_idx + 1]) = (s[left_idx + 1], s[left_idx])	
                    swap_count += 1
                else:
                    while (temp_right_idx < right_idx):
                        (s[temp_right_idx], s[temp_right_idx + 1]) = (s[temp_right_idx + 1], s[temp_right_idx])
                        temp_right_idx += 1
                        swap_count += 1

                    left_idx += 1
                    right_idx -= 1

        s = "".join(s)
    else:
        return -1
    
    return swap_count



if __name__ == "__main__":
    s = "nitni"
    s = "acabb"
    print(min_swap_palindrome(s))
