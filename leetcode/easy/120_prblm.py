"""
-> Find Minimum Operations to Make All Elements Divisible by Three

You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
Return the minimum number of operations to make all elements of nums divisible by three.

"""

class Solution:
    def miniOperations(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            if n % 3:
                res += 1
        return res

# Example usage
obj = Solution()
nums = [1, 2, 3, 4]
print(obj.miniOperations(nums))