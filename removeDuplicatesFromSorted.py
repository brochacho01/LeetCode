class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if a num is a duplicate, replace it with an out of range number, and count how many are placed, then do a loop using python list remove method
        # solution that requires 2 passes that only beats 5%
        # numDups = 0
        # lastNum = nums[0]
        # nLen = len(nums)
        # for i in range(1, nLen):
        #     if nums[i] == lastNum:
        #         nums[i] = -101
        #         numDups += 1
        #     else:
        #         lastNum = nums[i]
        # # Now remove duplicate elements
        # for i in range(numDups):
        #     nums.remove(-101)
        # return len(nums)
        i = 1
        nLen = len(nums)
        lastNum = nums[0]
        while i < nLen:
            if nums[i] == lastNum:
                nums.remove(lastNum)
                nLen = len(nums)
            else:
                lastNum = nums[i]
                i += 1
        return nLen