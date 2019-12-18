#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Implement int sqrt(int x). 

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x):
        left = 0
        right = x // 2 + 1 # Conside x = 1
        while left < right:
            mid = (left + right + 1) >> 1
            msquare = mid * mid
            if msquare > x:
                right = mid - 1
            elif msquare <= x:
                left = mid
        return left

x = 9
sol = Solution()
print(sol.mySqrt(x))
