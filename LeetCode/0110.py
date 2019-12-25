# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calLevel(self, node):
        return 0 if not node else max(self.calLevel(node.left), self.calLevel(node.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftLevel = self.calLevel(root.left)
        rightLevel = self.calLevel(root.right)
        if abs(leftLevel-rightLevel) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        