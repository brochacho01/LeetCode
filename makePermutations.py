class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # dfs solution
        result = []
        nLen = len(nums)
        numsUsed = [0]*nLen
        for i in range(nLen):
            self.dfs(nums, [], i, numsUsed.copy(), result)
        return result
    
    def dfs(self, nums, curList, curIndex, numsUsed, result):
        curList.append(nums[curIndex])
        numsUsed[curIndex] = 1
        if len(curList) == len(nums):
            result.append(curList)
            return
        else:
            for i in range(len(nums)):
                if numsUsed[i] == 0:
                    self.dfs(nums, curList.copy(), i, numsUsed.copy(), result)
        return