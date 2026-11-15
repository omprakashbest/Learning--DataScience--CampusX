"""
-> Destination City 

You are given the array paths, where path[i] = [cityAi, CityBi] means there exists a direct path going from
cityAi to cityBi. return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one 
distination city.

"""

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        s = set()
        for p in paths:
            s.add(p[0])
        
        for p in paths:
            if p[1] not in s:
                return p[1]
        


obj = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(obj.destCity(paths))