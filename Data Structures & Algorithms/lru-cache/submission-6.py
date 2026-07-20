# key will be in hashmap
class Node:
    def __init__(self, key=0, val=0, next=None, prev=None ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    # least recently used removed first
    # key val, implies hashmap
    # seems like a doubly linkedlist would be good here with a tail pointer
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # key: Node(val)
        self.nodes = {}

    def rmTail(self):
        node = self.tail.prev
        self.rmNode(node)
    
    def rmNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del self.nodes[node.key]

    def addNode(self, node):
        next = self.head.next
        self.head.next = node
        node.next = next
        node.prev = self.head
        next.prev = node
        self.nodes[node.key] = node

    # makes node head
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        self.rmNode(node)
        self.addNode(node)
        return node.val
        
    # update key if key exists, add otherwise, makes Node head
    def put(self, key: int, value: int) -> None:
        if self.capacity == len(self.nodes) and key not in self.nodes:
            self.rmTail()
        if key in self.nodes:
            self.rmNode(self.nodes[key])
        node = Node(key, value, None, None)
        self.addNode(node)


        
        
