# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Get the leftest and rightest node at each level and check the difference
    #BFS
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 1
        level = [(root, 0)]
        
        while len(level) != 0:
            res = max(res, level[-1][1]-level[0][1]+1)
            nextLevel = []
            for item, lev in level:
                if item.left:
                    nextLevel.append((item.left, 2*lev))
                if item.right:
                    nextLevel.append((item.right, 2*lev+1))
            level = nextLevel
            
        return res
        
        
