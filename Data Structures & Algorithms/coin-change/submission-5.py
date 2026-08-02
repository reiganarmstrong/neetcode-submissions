import sys
sys.setrecursionlimit(20000)
class Solution:
    # dollar coins, amount in dollars
    # fewest number of coins
    # dfs, memoization, amountLeft, cache, minimize, return up
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(amountLeft = amount, cache = {0: 0}):
            if amountLeft in cache:
                return cache[amountLeft]
            if amountLeft < 0:
                return float('inf')
            minim = float('inf')
            for coin in reversed(coins):
                minim = min(dfs(amountLeft - coin, cache) + 1, minim)
            cache[amountLeft] = minim
            return minim
        res = dfs()
        return res if res != float('inf') else -1
            
        