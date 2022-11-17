class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # You do this macro, because an overlapping segment is the distance between the greatest start and the smallest end
        # If there is no overlap, then the smallest end - the greatest start will be less than 0 thus will evaluate to 0
        xLap = max(min(ax2,bx2) - max(ax1,bx1), 0)
        yLap = max(min(ay2, by2) - max(ay1, by1), 0)
        overlap = yLap * xLap
        axLen = abs(ax2 - ax1)
        ayLen = abs(ay2 - ay1)
        bxLen = abs(bx2 - bx1)
        byLen = abs(by2 - by1)
        aA = axLen * ayLen
        bA = bxLen * byLen
        return aA + bA - overlap