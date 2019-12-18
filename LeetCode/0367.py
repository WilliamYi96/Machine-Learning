# Given a positive integer num, write a function which returns True if num is a perfect square else False.

class Solution:
    def isPerfectSquare(self, num):
        left = 0
        right = num // 2 + 1
        while left < right:
            mid = (left + right + 1) >> 1
            msquare = mid * mid
            if msquare == num:
                return True
            elif msquare > num:
                right = mid - 1
            elif msquare < num:
                left = mid
        return False