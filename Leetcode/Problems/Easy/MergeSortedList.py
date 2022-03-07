# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fhead = l1
        shead = l2
        dnode = ListNode(-1)
        temp = dnode
        
        while True:
            if fhead is None:
                temp.next = shead
                break
            if shead is None:
                temp.next = fhead
                break
            
            if fhead.val <= shead.val:
                temp.next = fhead
                fhead = fhead.next
            else:
                temp.next = shead
                shead = shead.next
            
            temp = temp.next
        
        return dnode.next
        
