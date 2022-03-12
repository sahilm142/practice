"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        curr = head
        
        #Visited Nodes
        nodes = {}
        
        if not head:
            return head
        
        #Create New Head and add it to nodes
        newHead = Node(head.val)
        nodes[head] = newHead
        
        temp = newHead
        
        while curr:
            #next node check
            if curr.next:
                #Check if the node is already created then point the current next to it else create new and add
                if curr.next in nodes:
                    temp.next = nodes[curr.next]
                else:
                    temp.next = Node(curr.next.val)
                    nodes[curr.next] = temp.next
            
            #random node check
            if curr.random:
                #if random node is not created yet create one and point the current random to this, else just use from existing list
                if curr.random not in nodes:
                    temp.random = Node(curr.random.val)
                    nodes[curr.random] = temp.random
                else:
                    temp.random = nodes[curr.random]
            
            temp = temp.next
            curr = curr.next
            
        
        return newHead
        
