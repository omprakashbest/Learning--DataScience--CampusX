"""
-> Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. if there is no such string,
return an empty string "".

A string is palindromic if it read the same forward and backward.

"""

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""

obj = Solution()
words = ["abc","car","ada","racecar","cool"]
print(obj.firstPalindrome(words))
