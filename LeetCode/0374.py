# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# Binary Search 0035, 0278, 0374

class Solution:
    def guessNumber(self, n):
        left = 0
        right = n - 1 
        res = -1
        while left<=right:
            mid = int( left + (right - left) / 2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid - 1
        res = left
        return res
                