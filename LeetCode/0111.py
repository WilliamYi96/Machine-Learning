# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # flag = True
    # def calMinDepth(self, root):
    #     if not root:
    #         return 0
        
    #     left = self.calMinDepth(root.left)
    #     right = self.calMinDepth(root.right)
    #     return min(left, right) + 1

    def calMaxDepth(self, root):
        if not root:
            return 0
        left = self.calMaxDepth(root.left)
        right = self.calMaxDepth(root.right)
        return max(left, right) + 1

    # def minDepth(self, root: TreeNode) -> int:
    #     if self.calMaxDepth(root) == 2:
    #         return 2
    #     else:
    #         return self.calMinDepth(root)
    def minDepth(self, root: TreeNode) -> int:
        if self.calMaxDepth(root) == 2:
            return 2
            
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1
        
            
