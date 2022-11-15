def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    sLen = len(s)
    curRow = 1
    rowsD = {}
    up = 1
    # Establish rows in dict where key is rowNum, val is string that the row should contain
    for i in range(numRows):
        rowsD.update({i+1: ""})
    for i in range(sLen):
        newString = rowsD.get(curRow)
        newString += s[i]
        rowsD.update({curRow : newString})
        # If we've hit last row, start going back up
        if curRow == numRows:
            up = -1
        if curRow == 1 and up == -1:
            up = 1
        if up == 1:
            curRow += 1
        else:
            curRow -= 1
    result = ""
    for i in range(numRows):
        result += rowsD.get(i+1)
    return result