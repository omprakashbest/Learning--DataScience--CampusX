"""
-> Maximum Sum Circular Subarray

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of hte array. Formally, the next element of 
nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. formally, for a subarray nums[i], 
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""

class Solution:
    def maxSubarraySumCircular(self, nums: list[int])-> int:
        curMax, curMin = 0, 0
        maxSum, minSum = nums[0], nums[0]
        res = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            res += n
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        return max(maxSum, res - minSum) if maxSum > 0 else maxSum

obj = Solution()
nums = [1,-2,3,-2]
print(obj.maxSubarraySumCircular(nums))