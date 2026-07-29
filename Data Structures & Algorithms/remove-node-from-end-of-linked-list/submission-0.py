# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = head
        numNodes  = 1
        while curr.next:
            numNodes += 1
            curr = curr.next
        print(numNodes)
        prev = dummy
        curr = head
        for _ in range(numNodes - n):
            prev = prev.next
            curr = curr.next
        prev.next = curr.next
        return dummy.next
            

