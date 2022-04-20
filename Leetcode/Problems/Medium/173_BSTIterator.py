# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.inOrder(root)
        
    #reverse Inorder: elements in stack will be sorted in desc order
    #pop element for next and to check hasNext check len of stack
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.right)
        self.arr.append(node.val)
        self.inOrder(node.left)

    def next(self) -> int:
        return self.arr.pop()
        

    def hasNext(self) -> bool:
        return len(self.arr)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

