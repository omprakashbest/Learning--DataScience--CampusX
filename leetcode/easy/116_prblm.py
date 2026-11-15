"""
-> Find X-Sum of All K-Long Subarrays Ⅰ

You are given an array nums of n integers and two integers k and x.
The x-sum of an array is calculated by the following procedure.

    • Count the occurrences of all elements in the array.
    • Keep only the occurrences of the top x most frequent elements. if two elements have the same number of 
    occurrences, the element with the bigger value is considered to be more frequent.
    • Calculate the sum of the resulting array.

Note: that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
"""

from collections import Counter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        res = []

        for i in range(len(nums) - k + 1):
            count = Counter(nums[i:i+k])

            if len(count) <= x:
                res.append(sum(nums[i:i+k]))
            else:
                pairs = list(count.items())
                pairs.sort(key=lambda p: (p[1], p[0]), reverse=True)
                cur_sum = 0
                for num, count in pairs[:x]:
                    cur_sum += (num * count)
                res.append(cur_sum)
        return res

# Example usage:
obj = Solution()
nums = [1,1,2,2,3,4,2,3]
k, x = 6, 2
print(obj.findXSum(nums, k, x))  

