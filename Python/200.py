from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        number_of_islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                row, col = queue.popleft()
                for dir_row, dir_col in directions:
                    new_row = row + dir_row
                    new_col = col + dir_col
                    if new_row in range(len(grid)) and \
                        new_col in range(len(grid[0])) and \
                        grid[new_row][new_col] == "1" and \
                        (new_row, new_col) not in visited:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == "1":
                    bfs(row, col)
                    number_of_islands += 1
                    visited.add((row, col))

        return number_of_islands


s1 = Solution()
print(s1.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
