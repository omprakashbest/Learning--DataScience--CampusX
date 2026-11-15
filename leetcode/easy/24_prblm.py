"""
-> Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd 
integers.

Return any array that satisfies this condition.
"""

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums