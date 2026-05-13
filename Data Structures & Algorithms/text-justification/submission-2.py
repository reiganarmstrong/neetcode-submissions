class Solution:
    def distributeSpacesCenter(self, arr, lineLen, maxWidth):
        lineLen -= len(arr)
        numSlots = max(1, len(arr) - 1)
        numSpaces = maxWidth - lineLen
        res = []
        for word in arr:
            res.append(word)
            if numSlots > 0:
                spaces = math.ceil(numSpaces/numSlots)
                res.append(" " * spaces)
                numSlots -= 1
                numSpaces -= spaces
        return "".join(res)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        i = 0
        stack = []
        lineLen = 0
        res = []
        while i < len(words):
            word = words[i]
            lineLen += len(word) + 1
            stack.append(word)
            if lineLen > maxWidth:
                if lineLen == maxWidth + 1:
                    res.append(" ".join(stack))
                    lineLen = 0
                    stack = []
                    i += 1
                else:
                    # only case where we do not increment
                    lineLen -= len(stack.pop()) + 1
                    res.append(self.distributeSpacesCenter(stack, lineLen, maxWidth))
                    lineLen = 0
                    stack = []
            else:
                i += 1

        if len(stack) > 0:
            spacesToAdd = " " * (maxWidth - lineLen)
            stack.append(spacesToAdd)
            res.append(" ".join(stack))
        
        return res

