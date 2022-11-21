class Solution:
    # checks to see how many jumps it takes to get to the end
    def jump(self, nums: List[int]) -> int:
        # This is a dp problem
        nLen = len(nums)
        dp = [0]*nLen
        # Want to iterate over all nums
        for i in range(nLen):
            ahead = nums[i]
            # want to update every jump ahead
            for j in range(i + 1, i + ahead + 1):
                if j > nLen - 1:
                    break
                # Update a cell if it hasn't been set, or if current path is more optimal than previously calculate path
                if dp[j] == 0 or dp[i] + 1 < dp[j]:
                    dp[j] = dp[i] + 1
                if j == nLen - 1:
                    return dp[j]
        return dp[nLen - 1]