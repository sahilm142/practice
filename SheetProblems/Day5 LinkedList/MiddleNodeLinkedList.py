# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #Soln 1. using naive approach
        # first calc total nodes, then midNode
        node = head
        midNode = head
        count = 0
        while node:
            node = node.next
            count+=1
        i=0
        midCount = count//2 
        while i<midCount:
            midNode=midNode.next
            i+=1
        return midNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #Soln 2. using first and second node
        # fnode will move by 1 step and snode by 2 step
        # when snode reaches end of the LL, fnode will be at mid
        fnode = head
        snode = head
        while snode and snode.next:
            fnode = fnode.next
            snode = snode.next.next
        return fnode


