class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxim = [0, 0]
        for idx, c in enumerate(s):
            # test odd pal
            l = idx - 1
            r = idx + 1
            while l >= 0 and r <= len(s) -1 and s[l] == s[r]:
                if r - l + 1 > maxim[1] - maxim[0] + 1:
                    maxim[0] = l
                    maxim[1] = r
                l -= 1
                r += 1

            # test even pal
            if idx < len(s) - 1:
                l = idx
                r = idx + 1
                while l >= 0 and r <= len(s) -1 and s[l] == s[r]:
                    if r - l + 1 > maxim[1] - maxim[0] + 1:
                        maxim[0] = l
                        maxim[1] = r
                    l -= 1
                    r += 1
        return s[maxim[0]: maxim[1] + 1]