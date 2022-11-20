class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # dynamic approach
        # there is n * m cells
        rLen = len(matrix[0])
        cLen = len(matrix)
        numCells = rLen * cLen
        result = []
        # start tracing over the input
        cellsCounted = 0
        i = 0
        j = -1
        # Just do 4 for loops
        while cellsCounted < numCells:
            # Start by going right
            for k in range(rLen):
                j += 1
                result.append(matrix[i][j])
                cellsCounted += 1
            cLen -= 1
            if cellsCounted == numCells:
                return result
            # Then go down
            for k in range(cLen):
                i += 1
                result.append(matrix[i][j])
                cellsCounted += 1
            rLen -= 1
            # Go left
            if cellsCounted == numCells:
                return result
            for k in range(rLen):
                j -= 1
                result.append(matrix[i][j])
                cellsCounted += 1
            cLen -= 1
            # go up
            if cellsCounted == numCells:
                return result
            for k in range(cLen):
                i -= 1
                result.append(matrix[i][j])
                cellsCounted += 1
            rLen -= 1
        return result