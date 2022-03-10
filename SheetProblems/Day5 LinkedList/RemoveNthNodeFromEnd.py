# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp = sp = head;
        
        #get the nth element from starting
        #when we'll do traversal it'll reach at the end of list 
        #and fp will reach to the nth item from end
        for _ in range(n):
            sp = sp.next
        #if item doesn't exist or it's a first element in the list
        if sp is None:
            return head.next
        
        while sp.next:
            sp = sp.next
            fp = fp.next
        fp.next = fp.next.next
        
        return head
        
        
