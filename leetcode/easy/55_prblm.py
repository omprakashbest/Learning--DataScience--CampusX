"""
-> Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.

"""

class Solution:
    def PowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n

obj = Solution()
n = 16
print(obj.PowerOfTwo(n))