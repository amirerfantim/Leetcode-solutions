from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[10 ** 100] * (cols + 1)] * (rows + 1)
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    continue
                dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]


s1 = Solution()
print(s1.minPathSum([[1,2,3],[4,5,6]]))
