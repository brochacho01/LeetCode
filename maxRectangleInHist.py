class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack based solution
        # Add a 0 to the heights so that once we reach the end, if there are elements in the stack then this forces all the areas to be calculated, beautiful
        heights.append(0)
        # Initialize a garbage element on the stack so that we know it's never empty, important for pop loops
        stack = [-1]
        maxA = 0
        for i in range(len(heights)):
            # If our current height is greater than last height on the stack, monotonic stack structure is broken, calculate rectangles and restore structure
            while heights[i] < heights[stack[-1]]:
                recH = heights[stack.pop()]
                # i - 1 is the right boundary of the rectangle
                # stack[-1] now represents the left boundary, so the width is rightbound - leftbound. Because while we're popping things off, our width is the beginning index up to excluding i
                recW = i - stack[-1] - 1
                maxA = max(maxA, recH*recW)
            # Once structure is restored, add index to stack
            stack.append(i)
        return maxA