class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # on each row that has start less than target, do binary search
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                # Do binary search
                if self.bSearch(matrix, target, i):
                    return True
        return False

    
    def bSearch(self, matrix, target, row):
        start = 0
        end = len(matrix[row]) - 1
        # print(row, start, end)
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False