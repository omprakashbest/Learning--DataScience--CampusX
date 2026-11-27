"""
-> 3Sum 

Given an integer array, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + 
nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threesum = val + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
    
obj = Solution()
nums = [-1,0,1,2,-1,-4]
print(obj.threeSum(nums))
