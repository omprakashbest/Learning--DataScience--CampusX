"""
-> Check if two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false 
otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        def Equal(s: list[str]):
                res = ""
                for ch in s:
                    res += ch
                return res
        return Equal(word1) == Equal(word2)


# Example: 
obj = Solution()
word1 = ["ab", "c"]
word2 = ["a", "gc"]
print(obj.arrayStringsAreEqual(word1, word2))