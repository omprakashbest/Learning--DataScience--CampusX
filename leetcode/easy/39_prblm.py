"""
-> Maximum Product Difference Between Two Pairs

The product difference between two pairs (a, b) and (c, d) is defined as (a * b)-(c * d).

• For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between
pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
"""

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        max1 = max2 = 0 # largest, second largest
        min1 = min2 = float("inf") # smallest , second smallest

        for n in nums:
            if n > max2:
                if n > max1:
                    max1, max2 = n, max1
                else:
                    max2 = n
            if n < min2:
                if n < min1:
                    min1, min2 = n, min1
                else:
                    min2 = n
        return (max1 * max2) - (min1 * min2)
    

obj = Solution()
nums = [5,6,2,7,4]
print(obj.maxProductDifference(nums))
