#question
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > len(result):
                        result = substring
        return result