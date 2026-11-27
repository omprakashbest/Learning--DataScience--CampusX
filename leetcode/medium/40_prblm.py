"""
-> Valid Sudoku 

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digit 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digit 1-9 without repetition.

Note:
    • A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    • Only the filled cells need to be validated according to the mentioned rules.

"""

from collections import defaultdict

from numpy import square


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r /3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c //3)]):
                    return False
                cols[c].add(board[r][c])
                rows[c].add(board[r][c])
                squares[(r // 3, c //3)].add(board[r][c])
        return True
                    