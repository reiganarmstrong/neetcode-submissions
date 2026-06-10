class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr=[], used=set()):
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    curr.append(num)
                    dfs(curr, used)
                    curr.pop()
                    used.remove(num)
        
        dfs()

        return res
