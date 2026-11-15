"""
-> The Two Sneaky Number of Digitville

In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1, 
each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional
time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two 
numbers (in any order), so peace can return to digitville.

"""

class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        x = 0

        # XOR all the numbers in the list and the range of numbers from 0 to n - 2
        for n in nums:
            x ^= n

        for i in range(len(nums) - 2):
            x ^= i

        diff_bit = x & -x
        xor1, xor2 = 0, 0
        for n in nums:
            if n & diff_bit:
                xor1 ^= n
            else:
                xor2 ^= n
        for i in range(len(nums) - 2):
            if i & diff_bit:
                xor1 ^= i
            else:
                xor2 ^= i

        return [xor2, xor1] 

obj = Solution()
nums = [0, 1, 1, 0]
print(obj.getSneakyNumbers(nums))  