# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        loop = True
        while loop:
            minim_ll = None
            minim_idx = -1
            for idx, ll in enumerate(lists):
                if not ll:
                    continue
                if not minim_ll or min(minim_ll.val, ll.val) == ll.val:
                    minim_ll = ll
                    minim_idx = idx
            
            if minim_ll == None:
                loop = False
            else:
                lists[minim_idx] = minim_ll.next

                curr.next = minim_ll
                curr = minim_ll
                curr.next = None

        return dummy.next


            



