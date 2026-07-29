from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        
        maxHeap = [[-val, key] for key, val in count.items()]
        heapify(maxHeap)
        out = []
        for _ in range(k):
            out.append(heappop(maxHeap)[1])
        return out