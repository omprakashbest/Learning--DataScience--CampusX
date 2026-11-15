"""
-> Check if All 1's Are at Least Length K place Away

Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other,
otherwise return false.

"""

class Solution:
    def klengthApart(self, nums: list[int], k: int) -> bool:
        spaces  = k

        for n in nums:
            if n == 1:
                if spaces < k:
                    return False
                spaces = 0
            else:
                spaces += 1
        return True        

obj = Solution()
nums, k = [1, 0, 0, 0, 1, 0, 0, 1], 2
print(obj.klengthApart(nums, k))
