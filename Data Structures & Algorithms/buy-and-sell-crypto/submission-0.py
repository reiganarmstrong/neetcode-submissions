class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minim = float('inf')
        for price in prices:
            newProfit = price - minim
            profit = max(profit, newProfit)
            minim = min(minim, price)
        return profit