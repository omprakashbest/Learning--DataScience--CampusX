"""
-> Covert an Array Into a 2D Array with Conditions

You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

• The 2D array should contain only the elements of the array nums.
• Each row in the 2D array contains distinct integers.
• The number of rows in the 2D array should be minimal.

Return the resulting array. if there are multiple answers, return any of them.

Note: that the 2D array can have a different number of elements on each row.

"""

from collections import defaultdict

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        count = defaultdict(int)
        res = []

        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])

            res[row].append(n)
            count[n] += 1
        return res
    
obj = Solution()
nums = [1, 3, 4, 1, 2, 3, 1]
print(obj.findMatrix(nums))