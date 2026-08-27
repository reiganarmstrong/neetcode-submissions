from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n + 1):
            adjList[i] = {}

        for source, target, time in times:
            adjList[source][target] = time
        
        visited = set()
        minHeap = [(0, k)]
        maxTime = 0
        while minHeap:
            time, source = heappop(minHeap)
            if source in visited:
                continue
            maxTime = max(maxTime, time)
            visited.add(source)
            for target in adjList[source]:
                if target in visited:
                    continue
                heappush(minHeap, (time + adjList[source][target], target))
        
        if (len(visited) < n):
            return -1
        
        return maxTime
            
            
