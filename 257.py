# 257. Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, currPath, res):
        currPath += "->%s" % root.val
        
        if not root.left and not root.right:
            res.append(currPath)
        else:
            if root.left:
                self.helper(root.left, currPath, res)
            if root.right:
                self.helper(root.right, currPath, res)
    
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        if not root:
            return []
        res = []
        currPath = "%s" % root.val
        if not root.left and not root.right:
            res.append(currPath)
        else:
            if root.left:
                self.helper(root.left, currPath, res)
            if root.right:
                self.helper(root.right, currPath, res)
        return res