from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return True
            
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            # print(p.val, q.val)
            if not self.check(p, q):
                return False
            if p:
                deq.append([p.left, q.left])
                deq.append([p.right, q.right])
        return True