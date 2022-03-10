# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1,c2 = l1,l2
        carr = 0
        temp = head = ListNode(0)
        
        while c1 or c2:
            summ = 0
            
            if c1 is not None:
                summ += c1.val
                c1 = c1.next
            if c2 is not None:
                summ += c2.val
                c2 = c2.next
            
            summ +=  carr
            carr = summ//10
            summ = summ - carr*10      
            
            temp.next = ListNode(summ)
            temp = temp.next
            
        if carr == 1:
            temp.next = ListNode(carr)
            temp = temp.next
        
        return head.next
            
        
