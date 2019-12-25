# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countLevel(self, node):
        level = 0
        if node == None:
            return 0

        while node != None:
            level += 1
            node = node.left
        return level

    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        leftLevel = self.countLevel(root.left)
        rightLevel = self.countLevel(root.right)
        # print(leftLevel, rightLevel)
        
        if leftLevel == rightLevel:
            return self.countNodes(root.right) + (1<<leftLevel)
        else:
            return self.countNodes(root.left) + (1<<rightLevel)
        