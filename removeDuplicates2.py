class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nLen = len(nums)
        # Return the value such that every index before that is in the valid result
        if nLen <= 2:
            return nLen
        k = 0
        prevNum = nums[0]
        numCount = 1
        for i in range(1, nLen):
            # Check for repeat number
            if nums[i] == prevNum:
                numCount += 1
                # If we've seen more than 2 of this number previously we must not copy this number and increase k
                if numCount > 2:
                    k += 1
                    nums[i] = '_'
                else:
                    nums[i - k] = nums[i]
            else:
                # If we're here, we didn't see the same number as the previous, thus update prev
                prevNum = nums[i]
                numCount = 1
                nums[i - k] = nums[i]
        return nLen - k