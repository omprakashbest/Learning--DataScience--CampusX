"""
-> Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold 

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and
average greater  than or equal to threshold.

"""

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
        return res

obj = Solution()
arr, k, threshold = [2,2,2,2,5,5,5,8], 3, 4
print(obj.numOfSubarrays(arr, k, threshold))