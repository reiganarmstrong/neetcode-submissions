import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for idx, coor in enumerate(points):
            dist = math.sqrt((coor[0])**2 + (coor[1])**2)
            distances.append((dist, idx))
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            res.append(points[heapq.heappop(distances)[1]])
        return res
