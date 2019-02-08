# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalancedHelper(self, root):
        if not root:
            return 0, True
        elif not root.left and not root.right:
            return 1, True
        LeftHeight, LeftFlag = self.isBalancedHelper(root.left)
        RightHeight, RightFlag = self.isBalancedHelper(root.right)
        CurrFlag = abs(LeftHeight-RightHeight)<=1 and LeftFlag and RightFlag
        return max(LeftHeight,RightHeight)+1, CurrFlag
            
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        Height, res = self.isBalancedHelper(root)
        return res