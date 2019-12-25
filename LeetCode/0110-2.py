class Solution:
    def calLevel(self, node):
        if not node: return 0
        left = self.calLevel(node.left)
        if left == -1: return -1
        right = self.calLevel(node.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left-right)<=1 else -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.calLevel(root) != -1
