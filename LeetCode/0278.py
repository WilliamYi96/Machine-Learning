# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Binary Search 0035, 0278

class Solution:
    # Linear Search O(n)
    def linearSearch(self, n):
        for i in range(n):
            if isBadVersion(i) == True:
                return i

    # Binary Search O(logn)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        res = -1
        while left<=right:
            mid = int((left+right)/2)
            if isBadVersion(mid) == False:
                left = mid + 1
            if isBadVersion(mid) == True:
                right = mid - 1
        res = left
        return res
            