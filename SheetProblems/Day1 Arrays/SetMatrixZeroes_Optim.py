class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #BruteForce: Mark which r,c needs to be zeroed
        #W/o using extra space, mark these r,c with some value
        #Use first row col to track which needs to be set to 0
        m,n = len(matrix),len(matrix[0])
        zero_row,zero_col = False,False
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    if r==0:
                        zero_row = True
                    if c==0:
                        zero_col = True
                    matrix[r][0]=matrix[0][c] = 0
                    
                            
        #Update all these 'r,c' to 0
        for r in range(1,m):
            for c in range(1,n):
                matrix[r][c] = 0 if matrix[0][c]==0 or matrix[r][0]==0 else matrix[r][c]
                
        #Check if first row or col has zero update them
        if zero_row:
            for i in range(n):
                matrix[0][i] = 0
        if zero_col:
            for j in range(m):
                matrix[j][0] = 0

