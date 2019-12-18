# Given a sorted (in ascending order) integer array nums of n elements and a target value, 

# write a function to search target in nums. If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums, target):
        res = [-1, -1]

        # find left bound
        left = 0
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            
            if left == len(nums):
                res[0] = -1
            elif nums[left] == target:
                res[0] = left
            else:
                res[0] = -1

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
            elif nums[left-1] == target:
                res[1] = left - 1
            else:
                res[1] = -1

        return res

# Another result
# Given a sorted (in ascending order) integer array nums of n elements and a target value, 

# write a function to search target in nums. If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums, target):
        res = [-1, -1]

        # find left bound
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            
            # if left == len(nums) - 1 or right == 0:
            #     res[0] = -1
            # else:
            #     res[0] = right + 1
            if right == len(nums) - 1:
                res[0] = -1
            elif nums[right+1] == target:
                res[0] = right+1
            else:
                res[0] = -1

        # find right bound 
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            
            if left == 0:
                res[1] = -1
            elif nums[left-1] == target:
                res[1] = left - 1
            else:
                res[1] = -1

        return res
                

                
