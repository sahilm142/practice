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
       

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        Inplace solution
        iterate over and keep track of min val node
        break the next of nodes and point to one which is minimum among two LL
        Swap after each iteration
        
        '''
        fhead = l1
        shead = l2
        if not fhead:
            return shead
        if not shead:
            return fhead
        
        if fhead.val>shead.val:
            fhead,shead = shead,fhead
            
        res = fhead
        
        while fhead and shead:
            temp = None
            while fhead and fhead.val<=shead.val:
                temp = fhead
                fhead = fhead.next
            temp.next = shead
            
            fhead,shead = shead, fhead
            
        return res
        
