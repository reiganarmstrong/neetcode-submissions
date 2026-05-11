class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        lookup = collections.defaultdict(int)
        for num in nums:
            total += num
            if total == k:
                res += 1
            
            if total - k in lookup:
                res += lookup[total - k]
            lookup[total] += 1
        return res