"""
-> Check Completeness of a Binary Tree 

Given the root of a binary tree, determine if it is a complete binary tree.

In a Complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last 
level are as far last as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while q: # Queue not empty
            # Remove front node
            node = q.popleft() 

            if node: # Is node None
                # add left and right child
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False
        return True


obj = Solution()
root = [1, 2, 3, 4, 5, 6]
print(obj.isCompleteTree(root)) 