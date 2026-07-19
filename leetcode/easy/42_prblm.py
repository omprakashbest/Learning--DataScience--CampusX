"""
-> Maximum Score After Splitting a String

Given a string 's' of zeros and ones, return the maximum score after splitting the string into two non-empty
substrings (i.e, left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones 
in the right substring.

"""

class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            
            res = max(res, zero + one)
        return res
    
obj = Solution()
s = "011101"
print(obj.maxScore(s))