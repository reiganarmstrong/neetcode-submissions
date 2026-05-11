class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(m1, n1, cache = {}):
            if (m1, n1) in cache:
                return cache[(m1, n1)]
            if min(m1, n1) < 0 or m1 >= m or n1 >= n:
                return 0
            if m1 == m - 1 and n1 == n - 1:
                return 1

            total = dfs(m1 + 1, n1, cache)
            total += dfs(m1, n1 + 1, cache)
            cache[(m1, n1)] = total
            return total
        
        return dfs(0, 0)
