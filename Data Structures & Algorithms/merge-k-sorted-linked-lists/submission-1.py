# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        minHeap = []
        for idx, ll in enumerate(lists):
            heapq.heappush(minHeap, [ll.val, idx])
        
        while len(minHeap) > 0:
            val, idx = heapq.heappop(minHeap)
            topNode = lists[idx]
            if topNode.next:
                heapq.heappush(minHeap, [topNode.next.val, idx])
                lists[idx] = lists[idx].next

            curr.next = topNode
            curr = curr.next
            curr.next = None
        
        return dummy.next
