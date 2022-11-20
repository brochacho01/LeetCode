class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic programming solution, based on recurrence
        nLen = len(nums)
        dp = [0]*nLen
        dp[0] = nums[0]
        for i in range(1, nLen):
        # Check to see if adding nums of i to current subarray is greater than just placing nums of i in dp and starting new subvector
            dp[i] = max(dp[i-1] + nums[i],nums[i])
        nMax = -10**4 - 1
        for i in range(nLen):
            if dp[i] > nMax:
                nMax = dp[i]
        return nMax