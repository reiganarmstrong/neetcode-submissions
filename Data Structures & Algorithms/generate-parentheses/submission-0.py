class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr=[], numOpen=0, numClose=0):
            if numOpen == numClose == n:
                res.append("".join(curr))
                return
            if numClose > numOpen or numOpen > n or numClose > n:
                return
            
            curr.append('(')
            dfs(curr, numOpen + 1, numClose)
            curr.pop()
            curr.append(')')
            dfs(curr, numOpen, numClose + 1)
            curr.pop()

            return
        dfs()
        return res