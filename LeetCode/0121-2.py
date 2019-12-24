import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = sys.maxsize
        maxProfits = 0
        for i in range(len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            else:
                if prices[i]-minValue > maxProfits:
                    maxProfits = prices[i] - minValue
        return maxProfits