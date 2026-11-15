"""
-> Shortest Path with Alternating Colors

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1.
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where :

    • redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, 
    and 

    • blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node
x such that the edge colors alternate along the path, or -1 if such a path does not exist.
"""

from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)
        
        answer = [-1 for _ in range(n)]
        q = deque()
        q.append([0, 0, None]) # [Node, length, prev_edge_color]
        visit = set()
        visit.add((0, None))

        while q:
            node, length, edgeColor = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if edgeColor != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append([nei, length + 1, "RED"])

            if edgeColor != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append([nei, length + 1, "BLUE"])
        return answer

# Example usage
obj = Solution()
n = 3
redEdges, blueEdges = [[0,1],[1,2]], []
print(obj.shortestAlternatingPaths(n, redEdges, blueEdges))