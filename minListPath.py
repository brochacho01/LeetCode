class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp solution that will run in O(n * m) time
        dp = []
        numRows = len(grid)
        rowLen = len(grid[0])
        for i in range(numRows):
            row = []
            for j in range(rowLen):
                row.append(0)
            dp.append(row)
        # Initialize first row, first col
        dp[0][0] = grid[0][0]
        for i in range(1, rowLen):
            dp[0][i] = grid[0][i] + dp[0][i - 1]
        for i in range(1, numRows):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        # Now fill in the rest of the dp list
        for i in range(1, numRows):
            for j in range(1,rowLen):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[numRows-1][rowLen-1]