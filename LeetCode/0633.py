# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

class Solution:
    def msquare(self, c):
        left = 0
        right = c // 2 + 1
        while left < right:
            mid = (left + right + 1) >> 1
            msquare = mid * mid
            if msquare == c:
                left = mid
            elif msquare > c:
                right = mid - 1
            elif msquare < c:
                left = mid
        return left

    def judgeSquareSum(self, c):
        # get the binary sqrt of c
        left = 0
        right = self.msquare(c)
        while left <= right:
            msum = left * left + right * right
            if msum == c:
                return True
            elif msum > c:
                right -= 1
            elif msum < c:
                left += 1
        return False
    

c = 4
sol = Solution()
print(sol.judgeSquareSum(c))
            
        