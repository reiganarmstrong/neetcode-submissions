class Node:
    def __init__(self):
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.head = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            
            curr = curr.children[c]
        
        curr.end = True



    def search(self, word: str) -> bool:
        curr = self.head
        # for c in word:
        #     if c in curr.children:
        #         curr = curr.children[c]
        #     else:
        #         return False
        # return curr.end
        
        def dfs(curr = self.head, i = 0):
            if i >= len(word):
                return curr.end
            c = word[i]

            if c in curr.children:
                return dfs(curr.children[c], i + 1)
            elif c == '.':
                for c in curr.children:
                    if dfs(curr.children[c], i + 1):
                        return True
            
            return False
        return dfs()

