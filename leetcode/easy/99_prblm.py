"""
-> Maximum Ascending SubArray Sum

Given an array of positive integers nums, return the maximum possible sum of an an strictly increasing 
subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.
"""

class Solution:
    def maxAscendingSum(Self, nums: list[int]) -> int:
        cur = nums[0]
        res = cur 

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur += nums[i]
            else:
                cur = nums[i]
            res = max(res, cur)
        return res

obj = Solution()
nums = [10, 20, 30, 5, 10, 50]
print(obj.maxAscendingSum(nums))