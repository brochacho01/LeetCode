class Solution:
    # Checks to see if can make it to the end
    def canJump(self, nums: List[int]) -> bool:
        # Jumping
        nLen = len(nums)
        # Idea is that if dp list contains any 0's in it, then the "chain" is broken, return false
        # Catch some corner cases
        if nLen == 1:
            return True
        elif nums[0] == 0:
            return False
        # Take a jump, then do the numReq strategy, will be O(n) in worst case
        i = 0
        while True:
            if i >= nLen - 1:
                return True
            curNum = nums[i]
            # take num and jump if not 0
            if curNum != 0:
                i += curNum
            # If curNum is 0 then we need to look backward to find a number to get past the 0
            # each time a number less than numReq is found, increment numReq and decrement j to keep searching
            # if a num >= numReq found, update i and take that jump
            else:
                numReq = 2
                j = i - 1
                isFound = False
                while j >= 0:
                    if nums[j] < numReq:
                        j -= 1
                        numReq += 1
                    else:
                        isFound = True
                        i = j + nums[j]
                        break
                if not isFound:
                    return False