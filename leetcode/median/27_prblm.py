"""
->  Minimum Fuel Cost to Report to the Capital

There is a tree (i.e., a connected, undirected graph with no cycle) structure country network consisting of n cities
numbered form 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads
where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi. 

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative.
The cost of traveling between two cities is on liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.
"""

from collections import defaultdict
import math

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        adj = defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node, parent):
            nonlocal res
            passengers = 0

            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    passengers += p
                    res += int(math.ceil(p / seats))
            return passengers + 1
        res = 0
        dfs(0, -1)
        return res 

obj = Solution()
roads = [[0, 1], [0, 2], [0, 3]]
seats = 5
print(obj.minimumFuelCost(roads, seats))

