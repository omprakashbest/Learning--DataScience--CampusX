"""
-> Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes 
with a value in the inclusive range [low, high].

Example: 

             10
            /  \
           5   15
          / \     \
         3   7     18    
"""

from typing import Optional

from git import Tree

class TreeNode:
    # Constructor
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int :

        if not root:
            return 0
        
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        return (
            root.val + 
            self.rangeSumBST(root.left, low , high) +
            self.rangeSumBST(root.right, low , high)
        )
    
# Tree Node

root = TreeNode(10)
# left side
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

# right side
root.right = TreeNode(15)
root.right.right = TreeNode(18)

obj = Solution()
low = 7
high = 15

print(obj.rangeSumBST(root, low, high))