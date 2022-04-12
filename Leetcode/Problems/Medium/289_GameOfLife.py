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


#Updating Inplace, storing indices in set
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [0, 0, -1, -1, -1, 1, 1, 1]
        dy = [-1, 1, -1, 0, 1, -1, 0, 1]

        row, col = len(board), len(board[0])

        indices = set()

        for i in range(row):

            for j in range(col):

                live_neighb = 0

                for k in range(len(dx)):
                    newi, newj = i+dx[k], j+dy[k]

                    if newi<row and newi>=0 and newj<col and newj>=0:
                        live_neighb += board[newi][newj]

                if (board[i][j] and (live_neighb<2 or live_neighb>3)) or (board[i][j] == 0 and live_neighb==3):
                    indices.add((i,j))


        for (i,j) in indices:
            board[i][j] = 0 if board[i][j] == 1 else 1


                        
#Inplace w/o storing indices
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [0, 0, -1, -1, -1, 1, 1, 1]
        dy = [-1, 1, -1, 0, 1, -1, 0, 1]

        row, col = len(board), len(board[0])

        for i in range(row):

            for j in range(col):

                live_neighb = 0

                for k in range(len(dx)):
                    newi, newj = i+dx[k], j+dy[k]

                    if newi<row and newi>=0 and newj<col and newj>=0 and abs(board[newi][newj])==1:
                        live_neighb += 1

                if board[i][j] == 1:
                    if (live_neighb<2 or live_neighb>3):
                        board[i][j] = -1       # 1 becomes 0 in next state
                elif live_neighb == 3:
                    board[i][j] = 2        # 0 becomes 1 in next state

        #Update the values back, if 2 -> 1 if -1 -> 0
        for i in range(row):
            for j in range(col):
                if board[i][j]==2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0


