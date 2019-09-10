"""
Given a Binary Search Tree and a target number, 
return true if there exist two elements in the BST such that their sum is equal to the given target.

# Solved on 09/10/2019 by William"""

# BFS

from collections import deque

def findTarget(root, k):
    queue = deque()
    queue.append(root)
    nums = []

    while queue:
        Queue = queue.popleft()

        if k - Queue.val in nums:
            return True 
        nums.append(Queue.val)

        if Queue.left:
            queue.append(Queue.left)
        if Queue.right:
            queue.append(Queue.right)
    
    return False