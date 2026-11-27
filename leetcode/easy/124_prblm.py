"""
-> Valid Palindrome 

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]

obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))