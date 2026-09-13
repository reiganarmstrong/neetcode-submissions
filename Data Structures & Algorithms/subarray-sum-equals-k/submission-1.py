from collections import defaultdict

class Solution:
    # iterate once
        # keep running total
        # if out += hashmap[k - currVal] if k - currVal in hashMap else 0
    # build hasmap {prevSum: countOccurances}
        # initialize with {0: 1}

    
    # subtract prefix sum such that val + total - prefixSum = k
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = 0
        total = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1
        for i, val in enumerate(nums):
            out += hashMap[total + val - k]
            total += val
            hashMap[total] += 1
        
        return out




