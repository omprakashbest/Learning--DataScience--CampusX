"""
-> Longest Substring Without Repeating Characters

Given a string s, find the length of th longest substring without duplicate characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

obj = Solution()
s = "abcabcbb"
print(obj.lengthOfLongestSubstring(s))