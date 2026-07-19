"""
-> Buy Two chocolates

You are given an integer array prices representing the prices of various chocolates in a store. You are also 
given a single integer money. which represents your initial amount of money.
 
You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You 
would like to minimize the sum of the prices of the two chocolates ou buy.

Return the amount of money you will have leftover after buying the two chocolates. if there is no way for you 
to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

"""

class Solution:
    def buyChocolates(self, prices: list[int], money: int) -> int:
        min1 = min2 = float("inf")

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
            
        leftover = money - min1 - min2
        return leftover if leftover >= 0 else money

obj = Solution()
prices = [1, 2, 2]
money = 3
print(obj.buyChocolates(prices, money))