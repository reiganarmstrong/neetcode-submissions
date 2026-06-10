import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.defaultdict(int)
        for s in tasks:
            counts[s] += 1
        # timestamp
        t = 0
        # numLeft
        maxHeap = [[-count, 0] for count in counts.values()]
        cooldown = collections.deque()
        heapq.heapify(maxHeap)
        while maxHeap:
            while len(cooldown) > 0 and cooldown[0][1] <= t:
                top = cooldown.popleft()
                heapq.heappush(maxHeap, top)

            currCount = - maxHeap[0][0]
            threshold = maxHeap[0][1]
            if threshold > t:
                t = threshold
            heapq.heappop(maxHeap)
            t += 1

            if currCount - 1 > 0:
                currCount -= 1
                threshold = t + n
                cooldown.append([-currCount, threshold])

            if not maxHeap and cooldown:
                top = cooldown.popleft()
                heapq.heappush(maxHeap, top)
                t = max(t, top[1])
        
        return t

