# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        stack = [root]
        res = []
        nextLevel = []
        currRes = []
        levelCount = 0
        while len(stack) > 0:
            levelCount += 1
            
            for i in range(len(stack)):
                node = stack.pop()
                currRes.append(node.val)
                if node.left and node.right:
                    if (levelCount %2 == 1):
                        nextLevel.append(node.left)
                        nextLevel.append(node.right)
                    else:
                        nextLevel.append(node.right)
                        nextLevel.append(node.left)
                elif node.right and not node.left:
                    nextLevel.append(node.right)
                elif node.left and not node.right:
                    nextLevel.append(node.left)
                else:
                    continue
            stack += nextLevel
            nextLevel = []
            res.append(currRes)
            currRes = []
        return res
