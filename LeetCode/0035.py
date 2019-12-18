# Given a sorted array and a target value, return the index if the target is found. 

# If not, return the index where it would be if it wre inserted in order.

# Binary Search 0035, 0278

class Solution: 
    # Robust solution O(logn)
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i 
        return len(nums)

    # Binary Search O(n)
    def BinarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        res = -1 # not found
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        res = left
        return res

minput = [1,3,5,6]
target = 5
sol = Solution()
output = sol.BinarySearch(minput, target)
print(output)
                

