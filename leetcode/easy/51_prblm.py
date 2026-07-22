"""
->  Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
due to some error, one of the numbers in s got duplicated to another number in the set, which result in 
repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

"""

from typing import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        res = [0, 0] # [duplicate, missing]

        count = Counter(nums)
        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i

        return res

obj = Solution()
nums = [1, 2, 2, 4]
print(obj.findErrorNums(nums))