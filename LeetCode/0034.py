"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

"""

class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = int(left + (right - left) / 2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid < target:
                left = mid + 1
            elif nums[mid] == target:
                
                