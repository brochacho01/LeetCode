class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        falseBox = True
        falseRow = True
        falseCol = True
        for i in range(9):
            falseBox = self.validateBoxes(board, i)
            falseRow = self.validateRows(board, i)
            falseCol = self.validateCols(board, i)
            if not(falseBox and falseRow and falseCol):
                return False
        return True
    
    def validateBoxes(self, board, boxNum):
        # dict to track seen vals
        vals = {}
        startX = 0
        startY = 0
        if boxNum % 3 == 0:
            if boxNum == 3:
                startY = 3
            elif boxNum == 6:
                startY = 6
        elif boxNum % 3 == 1:
            startX = 3
            if boxNum == 1:
                startY = 0
            elif boxNum == 4:
                startY = 3
            else:
                startY = 6
        else:
            startX = 6
            if boxNum == 2:
                startY = 0
            elif boxNum == 5:
                startY = 3
            else:
                startY = 6
        for i in range(startX, startX + 3):
            for j in range(startY, startY+3):
                if vals.get(board[i][j], -1) == -1:
                    if board[i][j] != '.':
                        vals.update({board[i][j] : 1})
                else:
                    return False
        return True

    def validateRows(self, board, rowNum):
        vals = {}
        for i in range(9):
            if vals.get(board[i][rowNum], -1) == -1:
                if board[i][rowNum] != '.':
                    vals.update({board[i][rowNum] : 1})
            else:
                return False
        return True

    def validateCols(self, board, colNum):
        vals = {}
        for i in range(9):
            if vals.get(board[colNum][i], -1) == -1:
                if board[colNum][i] != '.':
                    vals.update({board[colNum][i] : 1})
            else:
                return False
        return True