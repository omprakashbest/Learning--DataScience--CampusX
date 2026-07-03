"""
-> Number of Good Pairs

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.


Example:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""

from collections import Counter

class Solution:
    # First Solution
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = Counter(nums)
        res = 0

        for n, c in count.items():
            res += c *(c - 1) // 2
        return res
    
    # Second Solution
    def numIdenticalPairs2(self, nums: list[int]) -> int:
        res = 0
        count = {} 

        for n in nums:
            if n in count:
                res += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return res

obj = Solution()
nums = [1,2,3,1,1,3] 
print(obj.numIdenticalPairs(nums))
print(obj.numIdenticalPairs2(nums))
        