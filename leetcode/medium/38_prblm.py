"""
-> Group Anagrams 

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping char count to list of Anagrams
        
        for s in strs:
            count = [0]*26 # a...z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        return res.values()
    
obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))