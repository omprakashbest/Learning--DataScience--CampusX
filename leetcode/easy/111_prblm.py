"""
-> Maximum Value of an Ordered Triplet Ⅰ

You are given a 0-indexed integer array nums.

Return teh maximum value over all triplets (i, j, k) such that i < j < k. if all such triplets have a negative 
value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        res = 0
        N = len(nums)

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res

obj = Solution()
nums = [12,6,1,2,7]
print(obj.maximumTripletValue(nums))