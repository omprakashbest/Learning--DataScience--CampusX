"""
-> Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root
node reference(possibly updated) of the BST.

Basically, the deletion can be divided into two stages.
1. Search for a note to remove.
2. if the node is found, delete node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # find the min from right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root


obj = Solution()
# BST :- 
# root
root = TreeNode(5)
# left child
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
# right child
root.right = TreeNode(6)
root.right.right = TreeNode(7)
key = 3

result = obj.deleteNode(root, key)
print(result.left.val)        
print(result.left.left.val)        