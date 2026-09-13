from math import ceil
class Solution:
    # h hours to eat all bananas, must happen
    # each hour eat k bananas from a pile, pause afterwards
        # minimize k so that all bananas can still be eaten in h hours
    # 1 <= k <= max(piles)
    # n * logn
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minim = r
        while l <= r:
            m = (l + r) // 2

            numH = 0
            i = 0
            while numH < h and i < len(piles):
                numH += ceil(piles[i] / m)
                i += 1
            
            if numH <= h and i == len(piles):
                minim = min(minim, m)
                r = m - 1
            else:
                l = m + 1
        
        return minim
        