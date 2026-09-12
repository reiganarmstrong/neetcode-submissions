class Solution:
    def compress(self, chars: List[str]) -> int:
        # 2 pointers
        # k will be the next modifiable value (index), and will be output
        # will iterate through chars with i, inner while loop (j) that iterates until different char or end of list
        # modify vals in char starting at k, increment k
        # edge cases? I don't think so
        k = 0
        i = 0
        while i < len(chars):
            c = chars[i]
            j = i
            # have j be last consec char
            while j + 1 < len(chars) and chars[j + 1] == c:
                j += 1
            
            num = j - i + 1
            cArr = [c]
            # second case
            if num > 1:
                for d in str(num):
                    cArr.append(d)
            
            # sub chars vals
            for c in cArr:
                chars[k] = c
                k += 1
            
            i = j + 1

        return k
            
            
            