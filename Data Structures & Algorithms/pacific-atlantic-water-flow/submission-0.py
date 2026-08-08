class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()

        def dfs(coor, reachable):
            if coor in reachable:
                return

            reachable.add(coor)
            dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
            for dx, dy in dirs:
                newCoor = (coor[0] + dx, coor[1] + dy)
                if not (
                    min(newCoor) < 0
                    or newCoor[0] >= len(heights)
                    or newCoor[1] >= len(heights[newCoor[0]])
                ):
                    val = heights[coor[0]][coor[1]]
                    newVal = heights[newCoor[0]][newCoor[1]]
                    if newVal >= val:
                        dfs(newCoor, reachable)
        
        # vertical
        for i in range(len(heights)):
            # pac
            dfs((i, 0), pac)
            # atl
            dfs((i, len(heights[i]) - 1), atl)
        
        # horizontal top 
        for j in range(len(heights[0])):
            # pac
            dfs((0, j), pac)
        
        # horizontal bot
        for j in range(len(heights[len(heights) - 1])):
            # atl
            dfs((len(heights) - 1, j), atl)
        
        out = []
        for coor in atl:
            if coor in pac:
                out.append([coor[0], coor[1]])
        print(atl)
        print(pac)
        return out
