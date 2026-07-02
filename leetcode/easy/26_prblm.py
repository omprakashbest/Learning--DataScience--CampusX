"""
-> Reverse words in a string 

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
and initial word order.

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        l = 0
        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_l, temp_r = l, r - 1

                if r == len(s) - 1:
                    temp_r = r # temp_r += 1
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r + 1
        return "".join(s)



obj = Solution()
obj.reverseWords("Let's take LeetCode contest")