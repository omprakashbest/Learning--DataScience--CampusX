"""
-> Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in 
a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both string equal by performing at most one string swap on exactly one of 
the strings. Otherwise, return false.

"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indexes = [] # i, j

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)

            if len(indexes) > 2:
                return False

        if len(indexes) == 2:
            i, j = indexes
            return s1[i] == s2[j] and s1[j] == s2[i]

        return len(indexes) == 0

obj = Solution()
s1 = "bank"
s2 = "kanb"
print(obj.areAlmostEqual(s1, s2)) 