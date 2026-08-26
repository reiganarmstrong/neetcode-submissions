class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs take or skip, find max at idx, is that useful when landing on a idx?
        # for recursive call, we can just skip one on take, not skip on skip of curr
        # max at current in memo, where the i provided to dfs is assumed to be choosable
        def dfs(i = 0, cache = {}):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            maxVal = max(nums[i] + dfs(i + 2, cache), dfs(i + 1, cache))
            cache[i] = maxVal

            return cache[i]
        
        return dfs()