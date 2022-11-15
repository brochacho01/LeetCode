# Could be sped up by filling maxL and maxR at the same time using a while loop and doing calculations in same loop with separate indexes
def trap(self, height):
    hLen = len(height)
    # Will hold the value of the highest wall to the left of index i
    maxL = [0]*hLen
    # will hold the value of the highest wall to the right of index i
    maxR = [0]*hLen
    curWater = int(0)
    totalWater = int(0)
    # Want to iterate over height and find the highest walls to the left and right of i
    # This loop should fill maxL with values, therefore need to start at 1 because looking left and right and don't want to index out of bounds
    for i in range(1, hLen):
        maxL[i] = max(height[i - 1], maxL[i - 1])
    # Iterate over height backwards starting at len - 2, because going to look 1 to the right and don't want to index out of bounds. This should fill maxR with values. Go to -1 because exclusive
    for i in range(hLen - 2, -1, -1):
        maxR[i] = max(height[i + 1], maxR[i + 1])
    # At this point both of our max arrays are populated. So then for each index of height, we can calculate amount of water being held using the max height to the left and the right of i
    for i in range(hLen):
        curWater = min(maxL[i], maxR[i])
        # Need to check to see that the curWater is greater than the height at this point. i.e. if the walls to the left and right are shorter than we are, add no water. Also if we have any height at i, need to adjust water level
        if curWater >= height[i]:
            totalWater += curWater - height[i]
    return totalWater