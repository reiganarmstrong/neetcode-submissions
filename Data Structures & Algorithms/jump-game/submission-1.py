class Solution:
    # dfs, keep track of failed starting points
    # maximum jump length, we can jump less
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i = 0, failed = set()):
            # if this is true we can jump less
            if i >= len(nums) - 1:
                return True
            if i in failed:
                return False

            # 1 to max jump len
            for jmp in range(nums[i], 0, -1):
                if dfs(i + jmp, failed):
                    return True

            failed.add(i)
            return False            
        return dfs()