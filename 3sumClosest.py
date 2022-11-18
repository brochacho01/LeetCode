lass Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Try taking the 2pointer approach
        # Sort the array first, because for each combination if the next one is further away, we can stop checking because of the sort
        nums.sort()
        nLen = len(nums)
        # need to set up max, initialize to a size larger than the possible
        gMin = 2**32 - 1
        # Iterate over all nums
        for i in range(nLen):
            # Make sure i isn't ever the same number as a previous i, need to include the i != 0 to make sure we index bad values at the beginning of iterations
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            # Set up two pointers
            j = i + 1
            k = nLen - 1
            # Here we can start iterating over the two pointers
            while j < k:
                # Check our current sum
                curSum = nums[i] + nums[j] + nums[k]
                # Check first to see if we have an exact match
                if curSum == target:
                    return curSum
                # We can crunch our minDif and gMin
                # Idea here is that our current closest sum is stored in gMin, so if the difference between curSum and target is less than the difference between our current min and the target, then we want to update
                elif abs(curSum - target) < abs(gMin - target):
                    gMin = curSum
                # If our sum is less than target, we want to increment j as its value is guranteed to increase due to sorting the list previously
                if curSum < target: 
                    j += 1          
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                # Otherwise curSum is either == to or greater than target, so decrement k
                else: 
                    k -= 1
        return gMin