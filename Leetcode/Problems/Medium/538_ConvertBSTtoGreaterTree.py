# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseInorder(self, node):
        if not node:
            return

        self.reverseInorder(node.right)
        
        node.val += self.node_sum
        self.node_sum = node.val
        
        self.reverseInorder(node.left)
        
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        BST inorder gives sorted nodes val 
        for desc order do reverse inorder and calculate sum of nodes visited so far and add it to current node
        '''
        self.node_sum = 0
        self.reverseInorder(root)
        return root
        
