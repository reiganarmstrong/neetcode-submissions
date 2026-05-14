class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def valWorks(val):
            idx = 0
            hLeft = h
            while idx < len(piles) and hLeft > 0:
                currH = piles[idx]
                hLeft -= math.ceil(currH/val)
                idx += 1
            return idx == len(piles) and hLeft >= 0

        while l < r:
            m = (l + r) // 2
            if valWorks(m):
                r = m
            else:
                l = m + 1
        
        return r
