"""
-> Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

• NumArray(int[] nums) Initializes the object with the integer array nums.
• int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).

"""

class Solution:
    def __init__(self, nums: list[int]): # Constructor
        self.prefix = []  # List to store prefix sums
        cur = 0  # Running total
        for i in nums:  # Go through each number in nums
            cur += i  # Add current number to running total
            self.prefix.append(cur)  # Store running total in prefix list

    def sumRange(self, left: int, right: int) -> int:
        right_Sum = self.prefix[right]  # Sum from start to 'right'
        left_Sum = self.prefix[left - 1] if left > 0 else 0  # Sum before 'left' , Using this line comprehension in python
        return right_Sum - left_Sum  # Difference gives sum from left to right


#Example usage:
nums = [-2, 0, 3, -5, 2, -1]
obj = Solution(nums)
print(obj.sumRange(0, 2))  # Output: 1