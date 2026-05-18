class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def dfs(currIdx = 0, curr = []):
            if currIdx == len(nums):
                res.add(tuple(curr))
                return
            
            dfs(currIdx + 1, curr)

            curr.append(nums[currIdx])
            dfs(currIdx + 1, curr)
            curr.pop()
        
        dfs()

        return [list(tup) for tup in res]