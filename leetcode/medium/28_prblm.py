"""
-> As Far from Land as Possible 

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water 
cell such that its distance to the nearest land cell is maximized, and return the distance. if no land or water 
exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the database between two cells (x0, y0) and (x1, y1)
is |x0 - x1| + |y0 - y1|.

"""

from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        N = len(grid)
        q = deque()

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append((r, c))

        res = -1
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            res = grid[r][c]

            for dr, dc in direct:
                newR, newC = r + dr, c + dc
                if (min(newR, newC) >= 0 and max(newR, newC) < N and grid[newR][newC] == 0):
                    q.append((newR, newC))
                    grid[newR][newC] = grid[r][c] + 1
        return res -1 if res > 1 else -1

obj = Solution()
grid = [[1,0,1],[0,0,0],[1,0,1]]
print(obj.maxDistance(grid))