"""
-> Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false an integer n is a power of four,
if there exists an integer x such that n == 4x.

"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 4 != 0:
            return False
        
        return self.isPowerOfFour(n // 4)

# Example:
obj = Solution()
print(obj.isPowerOfFour(5))