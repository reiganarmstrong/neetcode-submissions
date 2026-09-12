import collections
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = collections.defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i
        
        out = []
        i = 0
        while i < len(s):
            c = s[i]
            k = last[c]
            j = i + 1
            while j < k:
                c2 = s[j]
                k = max(k, last[c2])
                j += 1
            out.append(k - i + 1)
            i = k + 1
        return out