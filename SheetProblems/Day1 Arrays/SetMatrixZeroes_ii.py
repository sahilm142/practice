class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #BruteForce: Mark which r,c needs to be zeroed
        #W/o using extra space, mark these r,c with some value
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for k in range(n):
                        if matrix[i][k]!=0:
                            matrix[i][k] = 's'
                    for k in range(m):
                        if matrix[k][j]!=0:
                            matrix[k][j] = 's'
                            
        #print(matrix)
        #Update all these 's' to 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 's':
                    matrix[i][j] = 0
