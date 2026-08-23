class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        def zero(i, j):
            # zero out col
            for k in range(rows):
                if matrix[k][j] != 0:
                    matrix[k][j] = 'a'

            # zero out row
            for k in range(cols):
                if matrix[i][k] != 0:
                    matrix[i][k] = 'a'

        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
        
