"""
-> Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""

class Solution:
    @staticmethod
    def my_sqrt(x):
        if x < 2:
            return x # 0 or 1 is it's own square root
        
        start = 1
        end = x // 2
        while start <= end:
            mid = start + (end - start) // 2
            # square = mid * mid
            
            if mid**2 == x:
                return mid
            elif mid**2 < x:  
                start = mid + 1
            else:
                end = mid - 1   
        return end
    
print(Solution.my_sqrt(75392))