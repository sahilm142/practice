class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #extreme left,right will get half of what other glasses will get
        #Distribute half of overflow from the one level up
        #Like Pascal Triangle
        triangle = [[0 for _ in range(query_glass+2)] for _ in range(query_row+1)]
        #print(triangle)
        triangle[0][0] = poured
        for i in range(query_row):
            for j in range(query_glass+1):
                overflow = max(triangle[i][j]-1, 0)
                triangle[i+1][j] += overflow/2
                triangle[i+1][j+1] += overflow/2
        
        return min(triangle[query_row][query_glass], 1)
        
