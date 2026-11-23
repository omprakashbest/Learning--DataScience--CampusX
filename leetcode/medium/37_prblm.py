"""
-> Flip String to Monotone Increasing 

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's 
(also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count0 = s.count('0')
        count1 = 0
        min_flips = count0

        for char in s:
            if char == '0':
                count0 -= 1
            else:
                count1 += 1
            min_flips = min(min_flips, count0 + count1)

        return min_flips

obj = Solution()
s = "00110"
print(obj.minFlipsMonoIncr(s))