"""
-> Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value
sequence.

           3
         /   \
        5     1
       / \   / \
      6   2 9   8
         / \
        7   4

for example: in the given tree above, the lead value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

"""

from turtle import right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            if root is None:
                return
            
            # leaf node
            if root.left is None and root.right is None:
                leaf.append(root.val)
                return
            
            # Traverse left and right
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2
    
# build Tree root-1
root1 = TreeNode(3)

root1.left = TreeNode(5)
root1.right = TreeNode(1)

root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)

root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

# build Tree Root-2 
root2 = TreeNode(3)

root2.left = TreeNode(5)
root2.right = TreeNode(1)

root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)

root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)

root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

obj = Solution()

print(obj.leafSimilar(root1, root2))