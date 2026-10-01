"""
-> Smallest Number With All Set Bits

You are given a positive integer n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains 
only set bits

"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 1
        while n > res:
            res = (res << 1) | 1
        return res

obj = Solution()
n = 5
print(obj.smallestNumber(n))