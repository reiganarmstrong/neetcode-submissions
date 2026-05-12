class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        def dfs(root):
            nonlocal numSet
            if root not in numSet:
                return 0
            count = 1
            numSet.remove(root)
            count += dfs(root + 1)
            count += dfs(root - 1)
            return count

        res = 0
        for num in nums:
            res = max(dfs(num), res)

        return res