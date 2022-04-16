class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if 0 <= i - 1 < m:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
                if 0 <= j - 1 < n:
                    dp[i][j] = dp[i][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
