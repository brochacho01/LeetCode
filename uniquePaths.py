class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    #    dfs approach is too slow
    # Take dp approach
    # Idea is to calculate the number of paths that exist to get to each cell
    # The following recurrence is created then:
    #  dp[i][j] == dp[i-1][j] + dp[i][j-1]
    # along the first row and first col only 1 path can reach those cells
    # runs in O(n*m) time and O(n*m) space
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == 0:
                    row.append(1)
                else:
                    row.append(0)
            dp.append(row)
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]