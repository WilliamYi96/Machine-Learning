# Running Time Exceed
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                curProf = prices[j]-prices[i]
                if curProf > maxProf:
                    maxProf = curProf
        return maxProf