"""
-> Longest Strictly Increasing or Strictly Decreasing Subarray 

You are given an array of integers nums. Return the length of the longest subarray of nums which is either 
strictly increasing or strictly decreasing.

"""

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        curr = 1
        res = 1
        increasing = 1

        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if increasing > 0:
                    curr += 1
                else:
                    curr = 2
                    increasing = 1
            elif nums[i-1] > nums[i]:
                if increasing < 0:
                    curr += 1
                else:
                    curr = 2
                    increasing = -1
            else:
                curr = 1
                increasing = 0 # reset the increasing/decreasing flag when equal elements are found
            res = max(res, curr)
        return res

obj = Solution()
nums = [1, 4, 3, 3, 2]
print(obj.longestSubarray(nums))  