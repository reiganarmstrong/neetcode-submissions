class Solution:
    # use smallest and find largest substring in larger text
    # memo = (str, smIdx, lgIdx) = maxLen
    # update memo after hitting bottom

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sm = text1 if len(text1) < len(text2) else text2
        lg = text1 if sm == text2 else text2
        def dfs(smIdx = 0, lgIdx = 0, cache = {}):
            if smIdx >= len(sm) or lgIdx >= len(lg):
                return 0
            # prevent repeated work
            if (smIdx, lgIdx) in cache:
                return cache[(smIdx, lgIdx)]
            
            if sm[smIdx] == lg[lgIdx]:
                cache[(smIdx, lgIdx)] = 1 + dfs(smIdx + 1, lgIdx + 1, cache)
            else:
                cache[(smIdx, lgIdx)] = max(dfs(smIdx, lgIdx + 1, cache), dfs(smIdx + 1, lgIdx, cache))
            return cache[(smIdx, lgIdx)]
        
        return dfs()
