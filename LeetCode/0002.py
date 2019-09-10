"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Solved on 09/10/2019 by William
"""

from collections import deque

def addTwoNumbers(l1, l2):
    dummy = ListNode(0); p = dummy
    carry = 0
    while l1 is not None or l2 is not None or carry != 0:
        sum_ = carry
        if l1 is not None:
            sum_ += l1.val
            l1 = l1.next
        if l2 is not None:
            sum_ += l2.val
            l2 = l2.next
        p.next = ListNode(sum_ % 10)  
        p = p.next
        carry = sum_ // 10
    return dummy.next

# Continue from here