"""
-> Path Crossing 

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north,
south, east, or west, respectively. You start at the origin (0,0) on a 2D plane and walk on the path
specified by path.

Return true if the path crosses itself a any point, that is, if at any time you are on a location you have 
previously visited. Return false otherwise.

"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
            "N": [0, 1],
            "S": [0, -1],
            "E": [1, 0],
            "W": [-1, 0]
        }
        visit = set() # (x, y)
        x, y = 0, 0

        for c in path:
            visit.add((x, y))
            dx, dy = dir[c]
            x, y = x + dx, y + dy
            if (x, y) in visit:
                return True
        return False

obj = Solution()
path = "NES"
print(obj.isPathCrossing(path))