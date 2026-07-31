class Solution:

    # binary search O(logn)
    # lVal <= mVal <= rVal; normal case
    # lVal <= mVal >= rVal; l and m on left side, r on i's own side
    # lVal >= mVal <= rVal; l on left side r and m on right side

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            lVal, rVal, mVal = nums[l], nums[r], nums[m]
            if mVal == target:
                return m
            print(l)
            print(r)
            print(m)
            print()
            print()
            print()
            # normal case
            if lVal <= mVal <= rVal:
                if mVal < target:
                    l = m + 1
                else:
                    r = m - 1
            # m on left
            elif lVal <= mVal > rVal:
                if mVal < target:
                    l = m + 1
                elif mVal > target:
                    if lVal > target:
                        l = m + 1
                    else:
                        r = m - 1
            # m on right
            elif lVal >= mVal < rVal:
                if mVal < target:
                    if target >= lVal:
                        r = m - 1
                    else:
                        l = m + 1
                elif mVal > target:
                    r = m - 1
        
        return -1

