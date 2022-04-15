# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getChildNode(self, node, low, high):
        if not node:
            return 
        
        if node.val<low:
            return self.getChildNode(node.right, low, high)
        
        if node.val>high:
            return self.getChildNode(node.left, low, high)
        
        node.left = self.getChildNode(node.left, low, high)
        node.right = self.getChildNode(node.right, low, high)
        
        return node
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        if node's val lies in between range fine
        else check for the one which lies in this range and make this its parent's children
        '''
            
        return self.getChildNode(root, low, high)
        
