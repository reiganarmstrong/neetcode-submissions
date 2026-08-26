class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        head = nums[:-1]
        tail = nums[1:]

        # dfs where i is acceptable to choose in arr
        # cache keeps track of max at each i for preventing repeated work
        def dfs(i, arr, cache):
            if i >= len(arr):
                return 0
            
            if i in cache:
                return cache[i]
            
            maxVal = max(arr[i] + dfs(i + 2, arr, cache), dfs(i + 1, arr, cache))

            cache[i] = maxVal

            return maxVal
        
        return max(dfs(0, head, {}), dfs(0, tail, {}))