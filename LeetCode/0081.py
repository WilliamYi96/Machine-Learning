# Runnin time: 68ms (70.98%), memory: 13.1MB (100%)

class Solution:
    def searchRotLeftBound(self, nums):
        mlength = len(nums)
        left = 0
        right = mlength - 1
        while left <= right:
            mid = (left + right) >> 1
            if mid == mlength - 1:
                return 0
            if nums[mid] > nums[mid+1]:
                return mid+1
            else:
                if nums[left] > nums[mid]:
                    right = mid - 1
                elif nums[left] == nums[mid]:
                    left += 1
                else:
                    left = mid + 1
        return 0

    def search(self, nums, target):
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False

        rotIndex = self.searchRotLeftBound(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            nmid = (mid + rotIndex) % len(nums)
            if nums[nmid] == target:
                return True
            elif nums[nmid] > target:
                right = mid - 1
            elif nums[nmid] < target:
                left = mid + 1
        return False
                
        