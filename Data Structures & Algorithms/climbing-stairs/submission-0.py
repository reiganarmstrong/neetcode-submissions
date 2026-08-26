class Solution:
    def climbStairs(self, n: int) -> int:
        # dfs, choose 1 or 2, dfs new target - option, return 1 if option counts otherwise return 0, cache target num options, so no target is checked multiple times
        def dfs(target = n, cache = {}):
            if target == 0:
                return 1
            if target in cache:
                return cache[target]
            if target < 0:
                return 0
            
            cache[target] = 0
            cache[target] += dfs(target - 1, cache)
            cache[target] += dfs(target - 2, cache)

            return cache[target]
        
        return dfs()