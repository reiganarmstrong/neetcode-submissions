class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        out = []
        inserted = False
        while i < len(intervals) and not inserted:
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                out.append(interval)
            elif interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            else:
                out.append(newInterval)
                out.append(interval)
                inserted = True
            i += 1
        if not inserted:
            out.append(newInterval)
        while i < len(intervals):
            out.append(intervals[i])
            i += 1

        return out