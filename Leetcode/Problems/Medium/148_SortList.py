# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. Traverse the linked list copy it in list
        # Sort the list, create linked list and return head
        
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        if n==0 or n==1:
            return head
        arr.sort()
        dnode = ListNode(-1)
        dnode.next = ListNode(arr[0])
        curr = dnode.next
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return dnode.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, l1, l2):
        dnode = ListNode(-1)
        curr = dnode
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        #If sub LL are of != length, point next to the pointer of not null LL
        if l1:
            curr.next = l1
            l1 = l1.next

        if l2:
            curr.next = l2
            l2 = l2.next
        return dnode.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1. Traverse the linked list copy it in list
        # Sort the list, create linked list and return head
        #2. Merge Sort?? Divide the LL in first half and second half
        #using 2pointer recursively then do mergesort on both of these parts, #Divide & Conquer

        #Base Condition for recursion
        if head is None or head.next is None:
            return head

        # Two Pointer approach to find the Middle Node in LL
        slow, fast = head, head
        temp = head

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        #Pointing the first half LL's last node to None
        temp.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeList(l1, l2)

