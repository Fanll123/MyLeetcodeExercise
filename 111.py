# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':

        if not root:
            return 0
        if not root.left or not root.right:
            return 1+max(self.minDepth(root.left),self.minDepth(root.right))
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))