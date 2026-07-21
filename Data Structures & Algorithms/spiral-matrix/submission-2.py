class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        null = -101

        def dfs(x=0, y=0, dirIdx=0):
            nonlocal out
            if min(x, y) < 0 or x >= len(matrix) or y >= len(matrix[x]) or matrix[x][y] == null:
                return
            out.append(matrix[x][y])
            matrix[x][y] = null

            i = dirIdx
            for _ in range(4):
                dx, dy = dirs[dirIdx]
                dfs(x + dx, y + dy, dirIdx)
                dirIdx += 1
                dirIdx %= 4

        dfs()
        return out
