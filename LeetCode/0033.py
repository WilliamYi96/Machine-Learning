class Solution:
    def searchRot(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if mid == len(nums) - 1:
                return 0
            # print(left, right, mid)
            if nums[mid] > nums[mid+1]:
                return mid+1
            elif nums[mid] < nums[mid+1]:
                if nums[left] < nums[mid]:
                    left = mid + 1
                elif nums[left] > nums[mid]:
                    right = mid - 1
                elif nums[left] == nums[mid]:
                    left = mid + 1
        return 0
                
    def search(self, nums, target):
        mlength = len(nums)
        if mlength == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        elif mlength == 0:
            return -1

        rotIndex = self.searchRot(nums)
        # print(rotIndex)

        left = 0
        right = mlength - 1
        while left <= right:
            mid = (left + right) >> 1
            nmid = (mid + rotIndex) % mlength
            if nums[nmid] == target:
                return nmid
            elif nums[nmid] > target:
                right = mid - 1
            elif nums[nmid] < target:
                left = mid + 1
        return -1