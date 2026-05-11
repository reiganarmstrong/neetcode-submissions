class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if(difference in prev):
                return [prev[difference], idx]
            prev[nums[idx]] = idx
        

            