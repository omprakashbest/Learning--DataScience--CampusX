"""
-> Find Missing and Repeated Values

You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n^2]. Each integer
appears exactly once except a which appears twice and b which is missing. the task is to find the repeating and 
missing number a and b.

Return a 0-indexed integer array ans fo size 2 where ans[0] equals to a and ans[1] equals to b.
"""

from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        N = len(grid)
        count = defaultdict(int)
        for i in range(N):
            for j in range(N):
                count[grid[i][j]] += 1

        double, missing = 0, 0

        for num in range(1, N*N + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num
        return [double , missing]

obj = Solution()
grid = [[1,3],[2,2]]
print(obj.findMissingAndRepeatedValues(grid))