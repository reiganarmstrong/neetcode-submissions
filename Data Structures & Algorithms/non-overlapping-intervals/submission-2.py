class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = [-float('inf')] * 2
        out = 0
        for start, end in intervals:
            if prev[1] > start:
                # if end is greater than prev end, update prev
                if end < prev[1]:
                    prev = [start, end]
                # increase out since this requires sub
                out += 1
            else:
                prev = [start, end]

        return out
            



