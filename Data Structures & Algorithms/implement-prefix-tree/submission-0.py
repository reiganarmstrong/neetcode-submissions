class Node:
    def __init__(self):
        self.end = False
        self.next = {}
class PrefixTree:

    def __init__(self):
        self.dummy = Node()

    def insert(self, word: str) -> None:
        curr = self.dummy
        for c in word:
            if c not in curr.next:
                curr.next[c] = Node()
            curr = curr.next[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.dummy
        for c in word:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.dummy
        for c in prefix:
            if c not in curr.next:
                return False
            curr = curr.next[c]
        return True
        