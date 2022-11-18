class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Try taking the 2pointer approach
        # Sort the array first, because for each combination if the next one is further away, we can stop checking because of the sort
        nums.sort()
        nLen = len(nums)
        # need to set up max, initialize to a size larger than the possible
        gMin = 2**32 - 1
        minDif = 2**32 - 1
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
                # print("fell in here")
                # Check our current sum
                curSum = nums[i] + nums[j] + nums[k]
                # print(nums[i], nums[j], nums[k], curSum)
                curDif = abs(target - curSum)
                # print(curDif)   
                # If the abs of the difference between sum and target is less than gMin, update gMin
                if curDif < minDif:
                    gMin = curSum
                    minDif = curDif
                # If our sum is less than target, we want to increment j as its value is guranteed to increase due to sorting the list previously
                if curSum < target:
                    # print("Fell into j inc")  
                    j += 1          
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                # Otherwise curSum is either == to or greater than target, so decrement k
                else: 
                    # print("fell into k dec")
                    k -= 1
        return gMin