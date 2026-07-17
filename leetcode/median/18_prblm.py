"""
-> Find Duplicate Subtree

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

"""

from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findDuplicatesSubtrees(self, root: Optional[TreeNode]):
        subtrees = defaultdict(list)
        res = []

        def dfs(node):
            if not node:
                return "null"
            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        dfs(root)
        return res
    

# ----------------------
# example tree
# ----------------------
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)

root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

root.right.left.left = TreeNode(4)

obj = Solution()
ans = obj.findDuplicatesSubtrees(root)

for node in ans:
    print(node.val)