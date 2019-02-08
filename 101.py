# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, left, right):
        if not left or not right:
            return left == right
        return self.helper(left.left, right.right) and self.helper(left.right, right.left) and left.val == right.val
    
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        
        if not root: return True
        
        return self.helper(root.left, root.right)