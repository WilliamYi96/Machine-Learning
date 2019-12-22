class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)

        while low <= high:
            mid = (low + high) >> 1
            curTotal = 0
            count = 1
            for element in nums:
                curTotal += element
                if curTotal > mid:
                    count += 1
                    curTotal = element
            if count > m:
                low = mid + 1
            else:
                high = mid - 1
        return low