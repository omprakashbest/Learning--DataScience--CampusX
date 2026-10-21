"""
-> Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The
trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    • You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the 
    amount of fruit each basket can hold.

    • Starting from any tree of your choice, you must pick exactly one fruit from every tree 
    (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    
    • Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given teh integer array fruits, return the maximum number of fruits you can pick.
"""

from collections import defaultdict

class Solution:
    def totalFruits(self, fruits: list[int]) -> int:
        count = defaultdict(int) # fruitType -> CountInBasket # HashMap
        l, total, res = 0, 0, 0 
        
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1
                if not count[f]:
                    count.pop(f)
            res = max(res, total)
        return res

obj = Solution()
fruits = [1, 2, 1]
print(obj.totalFruits(fruits))
