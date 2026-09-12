class Solution:
    # keep adding words to a line until maxWidth goes over
    # first word has no space prepending it, all others do.
    # join all words, but first calculate spaces to add to fill maxWidth
    # numSPaces = numWOrds - 1
    # wid = ciel(widthLeft / numSpaces)
    # widthLeft - wid
    # numSpaces -= 1
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        wordIdx = 0
        out = []
        while wordIdx < len(words):
            line = []
            line.append(words[wordIdx])
            width = len(line[0])
            # add 1 to account for space
            while wordIdx + 1 < len(words) and width + len(words[wordIdx + 1]) + 1 <= maxWidth:
                wordIdx += 1
                line.append(" " + words[wordIdx])
                width += len(line[-1])
            
            if wordIdx == len(words) - 1:
                line.append(" " * (maxWidth - width))
                out.append("".join(line))
            else:
                justifiedLine = []
                numSpaces = max(len(line) - 1, 1)
                for word in line:
                    justifiedLine.append(word)
                    if numSpaces > 0:
                        spaceLen = math.ceil((maxWidth - width) / numSpaces)
                        justifiedLine.append(" " * spaceLen)
                        numSpaces -= 1
                        width += spaceLen
                out.append("".join(justifiedLine))
            
            wordIdx += 1
        
        return out
