class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = [1] * len(nums)
        pref = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i + 1]
            suff[i] = suff[i + 1] * num

        for i in range(1, len(nums)):
            num = nums[i - 1]
            pref[i] = pref[i - 1] * num
        
        res = []
        for i in range(len(nums)):
            res.append(pref[i] * suff[i])
        
        return res
