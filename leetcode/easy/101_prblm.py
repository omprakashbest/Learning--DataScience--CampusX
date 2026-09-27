"""
-> Check If Array Is Sorted and Rotated

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some 
number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in the array B of the same length such that B[i] == A[(i+x) % 
A.length] for every valid index i.

"""

class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 1
        N = len(nums)

        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:
                count += 1
            else:
                count = 1
            
            if count == N:
                return True
            
        return N == 1

obj = Solution()
nums = [3, 4, 5, 1, 2]
print(obj.check(nums)) # Output: True
