class Solution:
    # brackets closed in lifo
    def isValid(self, s: str) -> bool:
        mappings = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        openC = set(mappings.values())
        stack = collections.deque()
        for c in s:
            if c in openC:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != mappings[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
                

        