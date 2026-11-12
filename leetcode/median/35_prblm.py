"""
-> Find Closest Node to Given two Nodes 

You are given a directed graph of n nodes numbered from 0 to n-1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i].
If there is no outgoing outgoing edge form i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance
from node1 to that node, and from node2 to that node is minimized. if there are multiple answers, return the node
with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.
"""

from collections import defaultdict, deque

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int)-> int:
        adj = defaultdict(list)
        for idx, val in enumerate(edges):
            adj[idx].append(val)

        def bfs(src, distMap):
            q = deque()
            q.append([src, 0])
            distMap[src] = 0
            while q:
                node, dist = q.popleft()
                for nei in adj[node]:
                    if nei not in distMap:
                        q.append([nei, dist + 1])
                        distMap[nei] = dist + 1

        node1Dist = {} # Map node = distance from node1
        node2Dist = {} # Map node -> distance from node2
        bfs(node1, node1Dist)
        bfs(node2, node2Dist)

        res = -1
        resDist = float("inf")
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                dist = max(node1Dist[i], node2Dist[i])
                if dist < resDist:
                    res = i
                    resDist = dist
        return res
    
obj = Solution()
edges, node1, node2 = [2,2,3,-1], 0, 1
print(obj.closestMeetingNode(edges, node1, node2))