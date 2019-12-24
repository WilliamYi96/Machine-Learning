# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# There are some errors of this code

class Solution:
    def __init__(self):
        self.cnt = True # true represents left, false represent right
        self.cnt1 = 0
        self.cnt2 = 0

    def findTarget(self, root, target, cnt):
        if root == None:
            return False, self.cnt1 if cnt else self.cnt2
        
        if cnt:
            self.cnt1 += 1
        elif not cnt:
            self.cnt2 += 1

        if root.val == target:
            return True
        elif root.val > target:
            self.findTarget(root.left, target, cnt)
        else:
            self.findTarget(root.right, target, cnt)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None:
            return False

        # make sure x < y   
        if x > y:
            x, y = y, x
        
        # Judge the interval (binary search)
        if x > root.val:
            self.isCousins(root.right, x, y)
        elif y < root.val:
            self.isCousins(root.left, x, y)
        
        xBound, cnt1 = self.findTarget(root.left, x, True)
        yBound, cnt2 = self.findTarget(root.right, y, False)

        if xBound and yBound and cnt1==cnt2 and cnt1!=0 and cnt2!=0:
            return True
        else:
            return False
