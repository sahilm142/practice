# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        if headA is None or headB is None:
                return None
        while currA is not currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next
            #if currA is None:
             #   currA = headB
            #else:
             #   currA = currA.next
            #if currB is None:
             #   currB=headA
            #else:
             #   currB = currB.next
        return currA
        
