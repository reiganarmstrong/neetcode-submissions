class Solution:
    # use smallest and find largest substring in larger text
    # memo = (str, smIdx, lgIdx) = maxLen
    # update memo after hitting bottom

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sm = text1 if len(text1) < len(text2) else text2
        lg = text1 if sm == text2 else text2
        def dfs(s = "", smIdx = 0, lgIdx = 0, cache = {}):
            if smIdx >= len(sm) or lgIdx >= len(lg):
                return len(s)
            # prevent repeated work
            if (s, smIdx, lgIdx) in cache:
                return cache[(s, smIdx, lgIdx)]
            
            maxVal = len(s)
            for i in range(smIdx, len(sm)):
                for j in range(lgIdx, len(lg)):
                    if sm[i] == lg[j]:
                        maxVal = max(maxVal, dfs(s + sm[i], i + 1, j + 1, cache))
                        break
            
            cache[(s, smIdx, lgIdx)] = maxVal
            return maxVal
        
        return dfs()
