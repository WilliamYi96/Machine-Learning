# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Typical module of Binary Tree Travesal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if root == None:
            return levels
        
        def helper(node, level):
            if level == len(levels):
                levels.append([])
            
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        
        helper(root, 0)
        return levels