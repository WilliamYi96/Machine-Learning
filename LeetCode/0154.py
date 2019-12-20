class Solution:
    def findMin(self, nums):
        mlength = len(nums)
        if mlength == 0:
            return -1

        left = 0
        right = mlength - 1
        while left <= right:
            mid = (left + right) >> 1
            if mid == mlength - 1:
                return nums[0]
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[left] > nums[mid]:
                    right = mid - 1
                elif nums[left] == nums[mid]:
                    left += 1
                elif nums[left] < nums[mid]:
                    left = mid + 1
        return nums[0]

# There is some problems of this file