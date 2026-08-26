class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        def dfs(i = 0, target = total / 2, failed = set()):
            if (target, i) in failed:
                return False

            if i >= len(nums) or target < 0:
                return False

            if target == 0 or nums[i] == target:
                return True
            
            if dfs(i + 1, target - nums[i], failed) or dfs(i + 1, target, failed):
                return True
            
            failed.add((target, i))
            return False
        return dfs()

