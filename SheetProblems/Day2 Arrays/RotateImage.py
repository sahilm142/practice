class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #BruteForce: Use one more Mat and copy
        #2. Transpose->Reverse each row
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        #print(matrix[2][::-1], r)
        for i in range(r):
            matrix[i] = matrix[i][::-1]
