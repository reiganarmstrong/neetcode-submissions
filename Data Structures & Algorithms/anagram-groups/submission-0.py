from collections import defaultdict
class Solution:
    # anagrams have exact same characters in any order
    # return output in any order
    # hashset or map
    # all lowercase
    # hashmap => tup(26 numbers) : list(str)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            tmp = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                tmp[idx] += 1
            
            tup = tuple(tmp)
            anagrams[tup].append(s)
        
        return list(anagrams.values())
