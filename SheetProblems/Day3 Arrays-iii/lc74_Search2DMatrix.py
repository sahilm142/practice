class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute Force
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target == matrix[i][j]:
                    return True
        return False    


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute Force
        #Binary Search: Sorted Matrix everyrow column
        #Check last element of each row
        #if greater than the value check that row for value
        m, n = len(matrix), len(matrix[0])
        ind = 0
        for i in range(m):
            if matrix[i][n-1]>=target:
                ind = i
                break
        for i in range(n):
            if matrix[ind][i] == target:
                return True


        return False

class Solution:
    def binarySearch(self, matrix, target, l, r, col):
        if l>r:
            return False
        mid = l+(r-l)//2
        print(l,r,mid, col)
        if matrix[mid//col][mid%col] == target:
            return True
        elif matrix[mid//col][mid%col]< target:
            return self.binarySearch(matrix, target, mid+1,r,col)
        else:
            return self.binarySearch(matrix, target, l, mid-1,col)
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute Force
        #Binary Search: Sorted Matrix everyrow column
        #Check last element of each row
        #if greater than the value check that row for value
        m, n = len(matrix), len(matrix[0])
        
        return self.binarySearch(matrix, target, 0, m*n-1, n)
        
