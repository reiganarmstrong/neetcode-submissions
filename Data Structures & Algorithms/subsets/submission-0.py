class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(currIdx = 0, curr = []):            
            if currIdx == len(nums):
                res.append(list(curr))
                return
            
            # exclude
            dfs(currIdx + 1, curr)

            # include
            curr.append(nums[currIdx])
            dfs(currIdx + 1, curr)
            curr.pop()

        dfs()
        return res
                
