"""
-> Divide Array Into Equal Pairs

You are given an integer array nums consisting of 2 * n integers.
You need to divide nums into n pairs such that:

• Each element belongs to exactly one pair.
• The elements present in a pair are equal.

Return true if nums can be divided into n pairs, otherwise return false.
"""

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = {} # Hashmap

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1

        for key, val in count.items():
            if val % 2:
                return False
        return True

obj = Solution()
nums = [3, 2, 3, 2, 2, 2]
print(obj.divideArray(nums))