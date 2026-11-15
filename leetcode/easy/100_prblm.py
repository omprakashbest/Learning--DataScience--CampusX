"""
-> Special Array Ⅰ

An array is considered special if the parity of every pair of adjacent elements is different. In Other Words, 
one element in each pair is must be even, and the other must be odd.

You are given an array of integers nums. Return true if the array is a special array. otherwise, return false.
"""

class Solution:
    def isSpecialArray(self, nums: list[int])-> bool:
        for i in range(1, len(nums)):
            # Check if the parity of the current element is the same as the previous element.
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True

obj = Solution()
nums = [2, 1, 4]
print(obj.isSpecialArray(nums)) 