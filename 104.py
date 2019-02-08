# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        