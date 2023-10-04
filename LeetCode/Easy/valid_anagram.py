"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_chars_s, count_chars_t = {}, {}
        for i in range(len(s)):
            count_chars_s[s[i]] = 1 + count_chars_s.get(s[i], 0)
            count_chars_t[t[i]] = 1 + count_chars_t.get(t[i], 0)
        
        for char in count_chars_s:
            if count_chars_s[char] != count_chars_t.get(char, 0):
                return  False
        
        return True