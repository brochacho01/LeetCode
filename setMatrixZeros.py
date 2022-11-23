class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = {}
        cols = {}
        numRows = len(matrix)
        rowLen = len(matrix[0])
        # Idea is to iterate over, and check what elements are zero, record their x and y, and then go back and zero out those ros/cols, O(n*m)
        for i in range(numRows):
            for j in range(rowLen):
                if matrix[i][j] == 0:
                    rows.update({i : i})
                    cols.update({j : j})
        # Now we've found all zeros, go back and zero out the rows/cols
        for row in rows.keys():
            for j in range(rowLen):
                matrix[row][j] = 0
        for col in cols.keys():
            for i in range(numRows):
                matrix[i][col] = 0