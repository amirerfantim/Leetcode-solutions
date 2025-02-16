class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1)] * (m + 1)
        dp[m - 1][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n -1:
                    continue
                dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
        return dp[0][0]


s1 = Solution()
print(s1.uniquePaths(3, 7))
