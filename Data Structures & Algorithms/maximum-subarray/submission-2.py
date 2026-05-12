class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        total = nums[0]
        maxSum = total
        while r < len(nums):
            total += nums[r]
            if total < nums[r]:
                l = r
                total = nums[r]

            maxSum = max(maxSum, total)
            r += 1
        
        return maxSum