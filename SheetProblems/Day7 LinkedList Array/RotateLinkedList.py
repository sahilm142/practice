# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Count no of nodes
        if not head or k==0 or not head.next:
            return head

        n=1
        curr = head
        while curr.next:
            curr=curr.next
            n+=1
        
        rotate=k%n
        #Point last to head
        curr.next=head        
        temp = newHead = head
        
        #find the turning point
        for _ in range(n-rotate):
            curr = curr.next
                
        head = curr.next
        #break the node b/w kth and (k+1)th Node else it'll be cycle
        curr.next = None
        
        
        return head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Count no of nodes
        n=0
        if not head or k==0:
            return head
        
        curr = head
        while curr:
            curr=curr.next
            n+=1
        if k>=n:
            k=k%n
        rotate = k#(k+1)%n
        
        if rotate == 0:
            return head
        
        temp = head
        
        #find the turning point
        for _ in range(n-rotate-1):
            if temp:
                temp = temp.next
                
        newHead=head
        
        if temp:
            newHead = temp.next
            temp.next = None
        else:
            return newHead
        
        t = newHead
        #traverse to last node and point next to head
        for _ in range(n-rotate, n):
            if t and t.next:
                t=t.next
            else:
                break
        if t:        
            t.next=head
        
        return newHead
