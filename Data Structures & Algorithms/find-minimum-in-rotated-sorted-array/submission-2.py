class Solution:
    # O(n) easy, just loop through
    # semi sorted, O(logn) binary search
    # l, r; nums[l] >= nums[r] means rotated
    # find m where nums[m-1] > nums[m]

    # case when all val same?
    # just make l > r end loop assume found min

    # might be going about this wrong
    # we want to know what side m is on
    # keep m on smaller side
    # if nums[l] < nums[m] < nums[r], all on same side, make r = m - 1
    # if nums[l] > nums[m] < nums[r], m on small side, make  r = m
        # will this cause a inf loop? we are gonna use // so no
    # if nums[l] < nums[m] > nums[r], m on large side, make l = m + 1
    # is this enough?
    # l will be our end case?
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            lVal, rVal = nums[l], nums[r]
            m = (l + r) // 2
            mVal = nums[m]
            if lVal <= mVal <= rVal:
                r = m - 1
            elif lVal >= mVal < rVal:
                r = m
            elif lVal <= mVal > rVal:
                l = m + 1
            else:
                print(lVal)
                print(mVal)
                print(rVal)
                assert(1 == 0)
        return nums[l]

        