# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr2 = arr.copy()
        arr2.reverse()
        return arr==arr2


class Solution:

    def reverse(self, node):
        curr = node
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev =curr
            curr = next
        node = prev
        return node

    def countNode(self, head):
        curr = head
        n=0
        while curr:
            curr=curr.next
            n+=1
        return n

    def palindrome(self, node1, node2):
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        count = self.countNode(head)
        mid = count//2

        #traverse to mid node
        curr = head
        i=0
        while curr and i<mid:
            curr = curr.next
            i+=1
        reverse_head = self.reverse(curr)

        return self.palindrome(head, reverse_head)
