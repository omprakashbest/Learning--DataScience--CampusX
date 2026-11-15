"""
-> Calculate Money in Leetcode Bank 

Hercy wants to save money for his first car. He puts money in the leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more 
than the day before. On every subsequent Monday. he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the leetcode bank at the end of the nth day.

"""

class Solution:
    def totalMoney(self, n: int) -> int:
        
        # 1+2+3+4+5+6+7 = 28
        # 2+3+4+5+6+7+8 = 28 + 7
        # ...

        day = 0
        deposit = 1
        res = 0

        while day < n:
            res += deposit 
            deposit += 1
            day += 1
            
            if day % 7 == 0:
                deposit = 1 + day // 7
        return res

# Example :
obj = Solution()
n = 7
print(obj.totalMoney(n))