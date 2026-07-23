"""
-> First Unique Character in a String 

Given a string s, find the first non-repeating character in it and return its index. if it does not exist return
-1.

"""

from collections import defaultdict

class Solution:
    def firstUnique(self, s: str) -> int:
        count = defaultdict(int) # char -> count

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

obj = Solution()
s = "leetcode"
print(obj.firstUnique(s))