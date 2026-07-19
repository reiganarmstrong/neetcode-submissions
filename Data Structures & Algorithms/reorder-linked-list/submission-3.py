# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # do not modify values
    # reorder list to 0, n-1, 1, n-2, 2, n-3
    # list len >= 1
    def reorderList(self, head: Optional[ListNode]) -> None:
        # dummy = ListNode(0, head)
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        l = 0
        r = len(arr) - 1
        start = end = None
        while l < r:
            start = arr[l]
            end = arr[r]
            next = start.next
            start.next = end
            end.next = next
            l += 1
            r -= 1
        
        if end:
            end.next.next = None