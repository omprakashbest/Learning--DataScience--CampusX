"""
-> Add to Array-Form of Integer

The array-form of an integer num is an array representing its digits in left to right order.

• For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

"""

class Solution:
    def AddTo_Array_form(self, nums, k):
        nums.reverse()
        i = 0
        while k:
            digit = k % 10 # digit is nothing but the remainder number of k 
            if i < len(nums):
                nums[i] += digit
            else:
                nums.append(digit)
            
            carry = nums[i] // 10
            nums[i] = nums[i] % 10

            k = k // 10
            k += carry
            i += 1
        nums.reverse()
        return nums
    

sol  = Solution()
sol.AddTo_Array_form([3, 4, 5, 6], 34)