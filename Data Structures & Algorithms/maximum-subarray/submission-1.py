class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        total = nums[0]
        maxSum = total
        while r < len(nums):
            if total + nums[r] < nums[r]:
                l = r
                total = nums[r]
            else:
                total += nums[r]
            maxSum = max(maxSum, total)
            r += 1
        
        return maxSum