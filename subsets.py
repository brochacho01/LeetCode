class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        nLen = len(nums)
        if nLen == 0:
            return result
        for i in range(nLen):
            self.dfs(nums, i, [], result)
        return result
    
    def dfs(self, nums, curIndex, curList, result):
        if curIndex == len(nums):
            return
        curList.append(nums[curIndex])
        result.append(curList)
        for i in range(curIndex+1, len(nums)):
            self.dfs(nums, i, curList.copy(), result)
        return