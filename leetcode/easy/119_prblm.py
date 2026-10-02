"""
-> Keep Multiplying Found Values by Two

You are given an array of integers nums. You are also given an integer original which is the first number
that needs to be searched for in nums.

You then do the following steps:

1. If original is found in nums, multiply it by two (i.e., set original = 2 * original).
2. Otherwise, stop the process.
3. Repeat this process with the new number as Long as you keep finding the number.

return the final value of original.
"""

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original

obj = Solution()
nums, original = [5, 3, 6, 1, 12], 3
print(obj.findFinalValue(nums, original))