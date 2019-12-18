# Given a sorted (in ascending order) integer array nums of n elements and a target value, 

# write a function to search target in nums. If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums, target):
        res = [-1, -1]

        # find left bound
        left = 0
        right = len(nums)
        while left<right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            
            if left == len(nums):
                res[0] = -1
            else:
                res[0] = left

        # find right bound 
        left = 0
        right = len(nums)
        while left<right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            
            if left == 0:
                res[1] = -1
            else:
                res[1] = left - 1

        return res
                
