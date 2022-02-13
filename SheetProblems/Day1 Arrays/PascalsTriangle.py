class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasList = []
        for i in range(numRows):
            subL = [1]*(i+1)
            for j in range(1,i):
                subL[j]=pasList[i-1][j-1]+pasList[i-1][j]
            pasList.append(subL)
        #print(pasList)
        return pasList
