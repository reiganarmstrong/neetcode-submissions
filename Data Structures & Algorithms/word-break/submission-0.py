class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i = 0, failed = set()):
            if i >= len(s):
                return True
            if i in failed:
                return False
            
            for word in wordDict:
                if i + len(word) - 1 > len(s) - 1:
                    continue
                
                substr = s[i: i + len(word)]
                if substr == word:
                    if dfs(i + len(word), failed):
                        return True
            
            failed.add(i)
            return False
        
        return dfs()

