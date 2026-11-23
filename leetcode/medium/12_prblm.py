"""
-> Construct Binary Tree From Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and 
postorder is the postorder traversal of the same tree, construct and return the binary tree.

"""

from git import Optional

class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        inorderIdx = {v:i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())

            idx = inorder.index(root.val)
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root

        return helper(0, len(inorder) - 1)    
    
