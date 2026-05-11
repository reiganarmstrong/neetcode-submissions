class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = {}
        t_counter = {}
        for idx in range(len(s)):
            s_counter[s[idx]] = s_counter.get(s[idx],0) + 1
            t_counter[t[idx]] = t_counter.get(t[idx],0) + 1
        if s_counter == t_counter:
            return True
        return False