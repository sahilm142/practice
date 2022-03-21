# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKNode(self, begin_node, end_node):
        curr = begin_node.next
        prev = begin_node
        
        dummy = curr
        
        while curr!=end_node:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt

        begin_node.next = prev
        
        new_begin_node.next = curr
        
        return new_begin_node
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k==1:
            return head
        
        dnode = ListNode(-1)
        
        dnode.next = head
        
        begin_node = dnode
        i=0
        while head:
            i+=1
            if i%k==0:
                #print(i, begin_node.val, head.next.val)
                begin_node = self.reverseKNode(begin_node, head.next)
                #print(begin_node.next)
                head = begin_node.next
            else:
                head = head.next
        
        return dnode.next
