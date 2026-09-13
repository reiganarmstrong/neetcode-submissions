class Solution:
    # prefix sum
    # suffix sum
    # see if val at either is equal
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]
        
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
        
        return -1
        