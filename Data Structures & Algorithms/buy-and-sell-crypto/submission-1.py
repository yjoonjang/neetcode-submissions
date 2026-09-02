class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0

        while len(prices) > 1:
            l = prices.pop(0)
            profit = max(prices) - l
            if profit > maxValue:
                maxValue = profit

            

        return maxValue
            