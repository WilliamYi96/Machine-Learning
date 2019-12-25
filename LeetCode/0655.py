# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calLevel(self, root):
        return 0 if root == None else max(self.calLevel(root.left), self.calLevel(root.right)) + 1
    
    def updateOutput(self, node, row, left, right):
        if node == None:
            return 
        mid = (left + right) >> 1
        self.res[row][mid] = str(node.val)
        self.updateOutput(node.left, row+1, left, mid-1)
        self.updateOutput(node.right, row+1, mid+1, right)

    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.calLevel(root)
        width = (1<<height) - 1
        self.res = [[""] * width for i in range(height)]
        self.updateOutput(root, row=0, left=0, right=width-1)
        return self.res