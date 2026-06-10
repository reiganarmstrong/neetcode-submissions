from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(idx = 0, curr = [], currSum = 0):
            if currSum == target:
                res.append(curr.copy())
                return
            if idx >= len(candidates) or currSum > target:
                return
            nextIdx = idx
            while nextIdx < len(candidates) and candidates[idx] == candidates[nextIdx]:
                nextIdx += 1
            curr.append(candidates[idx])
            currSum += candidates[idx]
            dfs(idx + 1, curr, currSum)
            curr.pop()
            currSum -= candidates[idx]
            dfs(nextIdx, curr, currSum)
        dfs()
        return res