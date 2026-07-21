# l and r pointer
# sliding window
# smaller increments in
# if both equal that is max possible area so both increment in
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            lH = heights[l]
            rH = heights[r]
            area = (r - l) * min(lH, rH)
            maxArea = max(maxArea, area)

            if lH > rH:
                r -= 1
            else:
                l += 1
        return maxArea

        