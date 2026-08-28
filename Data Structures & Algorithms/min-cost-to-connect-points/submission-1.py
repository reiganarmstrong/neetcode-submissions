from heapq import heappush, heappop

class Solution:
    # min spanning tree: cost = manhattan distance between a point and all other points
    # generate adj list
    # run primms algo (similar to djikstras)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        adjList = {}
        for x, y in points:
            if (x, y) not in adjList:
                adjList[(x, y)] = {}
            for x2, y2 in points:
                if (x, y) == (x2, y2):
                    continue
                adjList[(x, y)][(x2, y2)] = abs(x - x2) + abs(y - y2)
        

        visited = set()
        start = (points[0][0], points[0][1])
        visited.add(start)
        minCost = 0
        minHeap = []
        for dest in adjList[start]:
            cost = adjList[start][dest]
            heappush(minHeap, (cost, start, dest))

        while len(visited) < len(points):
            cost, start, dest = heappop(minHeap)
            if dest in visited:
                continue
            
            minCost += cost
            visited.add(dest)
            for nextDest in adjList[dest]:
                if nextDest not in visited:
                    cost = adjList[dest][nextDest]
                    heappush(minHeap, (cost, dest, nextDest))
        
        return minCost



