"""
-> Last Stone Weight ||

You are given an array of integers stones where stones[i] is the weight of the ith stone.

we are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose
the stones have weights x and y with x<=y. The result of this smash is :

• If x == y, both stones are destroyed, and
• If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
"""
import math
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total)) 
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total), 
                                dfs(i + 1, total + stones[i]))
            return dp[(i, total)]
        
        dp = {}
        return dfs(0, 0)