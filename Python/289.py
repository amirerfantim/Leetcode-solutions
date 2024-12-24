from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                live_neighbors = 0
                for dx, dy in directions:
                    if 0 <= row + dx < len(board) and 0 <= col + dy < len(board[0]):
                        if board[row + dx][col + dy] == 1 or board[row + dx][col + dy] == -1:
                            live_neighbors += 1

                if board[row][col] == 1 or board[row][col] == -1:
                    if live_neighbors > 3 or live_neighbors < 2:
                        board[row][col] = -1
                if board[row][col] == 0 or board[row][col] == 2:
                    if live_neighbors == 3:
                        board[row][col] = 2

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0


s1 = Solution()
print(s1.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
