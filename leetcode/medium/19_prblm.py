"""
-> Ones and Zeroes 

You are given an array of binary strings strs and two integers m and n.
return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

"""

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # memoization
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            
            mCnt, nCnt = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)

            if mCnt <= m and nCnt <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - mCnt, n - nCnt))
            return dp[(i, m, n)]
        
        return dfs(0, m, n)
    
obj = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(obj.findMaxForm(strs, m, n))
