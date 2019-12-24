# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parents = {}
        depths = {}
        def dfs(node, par = None):
            if node:
                depths[node.val] = 1 + depths[par.val] if par else 0
                parents[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        return depths[x]==depths[y] and parents[x]!=parents[y]

                
