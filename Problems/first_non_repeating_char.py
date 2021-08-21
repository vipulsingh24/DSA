"""
aaabccccdeeeed -> b
abcbad -> c
abcabcabc -> _
"""

"""
def get_first_non_repeating_char(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char in s:
        if char_counts[char] == 1:
            return char

    return "_"
"""
def get_first_non_repeating_char(s):
    char_counts = [0] * 26
    for char in s:
        char_counts[ord(char) - ord('a')] += 1

    print(char_counts)
    for char in s:
         if char_counts[ord(char) - ord('a')] == 1:
            return char
    return "_"



if __name__ == "__main__":
    str_ = "aaabccccdeeeed"
    print(get_first_non_repeating_char(str_))
