"""
-> Largest Substring between Two Equal Characters

Given a string, return the length of the longest substring between two equal characters, excluding the two
characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {} # char -> first index
        res = -1

        for i, c in enumerate(s):
            if c in char_index:
                res = max(res, i - char_index[c] - 1) 
            else:
                char_index[c] = i 

        return res

obj = Solution()
s = "abca"
print(obj.maxLengthBetweenEqualCharacters(s))