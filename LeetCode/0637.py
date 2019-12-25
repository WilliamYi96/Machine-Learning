# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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

        avgLevels = [0] * len(levels)

        for i in range(len(levels)):
            curSum = 0
            for j in range(len(levels[i])):
                curSum += levels[i][j]
            avgLevels[i] = curSum / len(levels[i])
        
        return avgLevels
