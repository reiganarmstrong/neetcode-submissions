class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dfs(l = 0, r = len(s) - 1, delUsed = False):
            if l >= r:
                return True
            
            c1 = s[l]
            c2 = s[r]

            if c1 == c2:
                return dfs(l + 1, r - 1, delUsed)
            elif delUsed:
                return False
            else:
                if dfs(l + 1, r, True) or dfs(l, r - 1, True):
                    return True
                return False
        
        return dfs()