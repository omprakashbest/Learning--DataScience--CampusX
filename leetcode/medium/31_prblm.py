"""
-> Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root 
node the BST after the insertion. it is guaranteed that the new value does not exist in the original BST.

Notice that here may exist multiple valid ways for the insertion, as long as the tree remains a BST after 
insertion. You can return any of them.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

obj = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
val = 5

# res = obj.insertIntoBST(root, val)

# print(res.val)             # 4
# print(res.right.val)       # 7
# print(res.right.left.val)  # 5