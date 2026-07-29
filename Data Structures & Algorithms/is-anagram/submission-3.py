class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = collections.defaultdict(int)
        countT = collections.defaultdict(int)
        for c in s:
            countS[c] += 1
        for c in t:
            countT[c] += 1
        return countS == countT