"""
-> Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column 
indices.

"""

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0]* ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
        return res

obj = Solution()
matrix = [[1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]]

print(obj.transpose(matrix))