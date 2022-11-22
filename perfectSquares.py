class Solution:
    def numSquares(self, n: int) -> int:
        # take a dp approach
        # The idea is that each index of dp represents a value, and the value stored at that index is the optimal number of squares that sum to that number
        dp = [10001] * (n + 1)
        dp[0] = 0
        index = 1
        # while our square value is less than n, because no point in checking if square is greater than n as it can't be used. Start at 1 as that's the minimum possible square
        while index * index <= n:
            square = index * index
            # iterate from square to n to see if incorporating new square is more efficient than previous most efficient
            for i in range(square, n+1):
                # Do the check by indexing i - square, which is val - square, and see if the num + 1 at that index is less than existing min
                dp[i] = min(dp[i - square] + 1, dp[i])
            # Once dp has been updated for current square, move to next square
            # print(dp)
            index += 1
        # Once the while loop is done, the most efficient path should be stored at dp[n]
        return dp[n]