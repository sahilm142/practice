class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #BruteForce: Mark which r,c needs to be zeroed
        rc = set()
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rc.add((i,j))
        #print(rc)
        for r,c in rc:
            #print(r,c)
            matrix[r]=[0]*n
            for i in range(m):
                matrix[i][c] = 0
                
            
