# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        i=1

        while slow and i<k:
            slow = slow.next
            i+=1
        #print(slow.val, fast.val)
        
        fast2 = slow

        while fast2.next:
            fast2 = fast2.next
            fast = fast.next
        slow.val, fast.val = fast.val, slow.val
        
        #print(slow.val, fast2.val)
        
        return head
