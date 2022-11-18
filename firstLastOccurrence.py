class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nLen = len(nums)
        result = []
        curI = -1
        for i in range(nLen):
            if curI == -1 and nums[i] == target:
                result.append(i)
                curI = i
            elif nums[i] == target:
                curI += 1
            elif curI != -1:
                result.append(curI)
                return result
        if curI != -1 and len(result) != 0:
            result.append(curI)
            return result
        else:
            result.append(-1)
            result.append(-1)
            return result