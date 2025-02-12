from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def capture(row, col):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
                board[row][col] = "T"
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    capture(dr + row, dc + col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                    if board[row][col] == "O":
                        capture(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"


s1 = Solution()
print(s1.solve([["O"]]))
