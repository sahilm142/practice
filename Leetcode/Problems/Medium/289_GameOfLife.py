class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [0, 0, -1, -1, -1, 1, 1, 1]
        dy = [-1, 1, -1, 0, 1, -1, 0, 1]
        
        row, col = len(board), len(board[0])
        
        res = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            
            for j in range(col):
                
                ln,tn=0,0
                
                for k in range(len(dx)):
                    newi, newj = i+dx[k], j+dy[k]
                    
                    if newi<row and newi>=0 and newj<col and newj>=0:
                        ln += board[newi][newj]
                        tn+=1

                if board[i][j] and (ln==2 or ln==3):
                    res[i][j]=1
                
                elif board[i][j]==0 and ln==3:
                    res[i][j]=1
                    
        board[:]=res[:]                    
                        
                        
