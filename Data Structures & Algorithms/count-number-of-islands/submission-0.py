class Solution:
    # counting islands
    # all edges are water
    # disregard diagonals
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            nonlocal grid
            if x >= len(grid) or y >= len(grid[x]) or min(x, y) < 0 or grid[x][y] == "0":
                return False
            
            grid[x][y] = "0"
            deltas = ((0, 1), (1, 0), (-1, 0), (0, -1))
            for dx, dy in deltas:
                dfs(x + dx, y + dy)
            
            return True
        
        num = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if dfs(x, y):
                    num += 1
        
        return num