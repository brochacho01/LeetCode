def maxArea(self, height):
    low = int(0)
    high = int(len(height) - 1)
    max = int(0)
    while(low < high):
        cur = min(height[low], height[high]) * (high - low)
        if cur > max:
            max = cur
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    return max