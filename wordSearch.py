class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # The idea is to look for each starting character, then look at all characters around it for the next character and so on
        # Slightly different idea, don't store visited, directly edit the board that you have seen
        numRows = len(board)
        rowLen = len(board[0])
        # An optimization is to first check to see if there are valid characters in the matrix
        chars = {}
        for i in range(len(word)):
            if chars.get(word[i], -1) == -1:
                chars.update({word[i] : 1})
            else:
                chars.update({word[i] : chars.get(word[i]) + 1})
        # iterate over matrix, each time a character in word is found, decrement that counter in the dict at the end if > 0 that means the word cannot exist
        for i in range(numRows):
            for j in range(rowLen):
                if chars.get(board[i][j], -1) != -1:
                    chars.update({board[i][j] : chars.get(board[i][j]) - 1})
        # Check validity
        for value in chars.values():
            if value > 0:
                return False
        # Look for starting char
        for i in range(numRows):
            for j in range(rowLen):
                if board[i][j] == word[0]:
                    if self.search(board, i, j, word, 1):
                        return True
        # If we've made it down here, then word does not exist, return false
        return False
        
    def search(self, board, i, j, word, curChar):
        if curChar == len(word):
            return True
        tmp = board[i][j]
        board[i][j] = '#'
        # Need to look up, down, left, right for next char in word
        #Look left if applicable
        if j > 0:
            if board[i][j-1] == word[curChar]:
                if self.search(board, i, j-1, word, curChar + 1):
                    return True
        # Look right if applicable
        if j < len(board[0]) - 1:
            if board[i][j + 1] == word[curChar]:
                if self.search(board, i, j+1, word, curChar+1):
                    return True
        # Look up if applicable
        if i > 0:
            if board[i - 1][j] == word[curChar]:
                if self.search(board, i-1, j, word, curChar+1):
                    return True
        # Look down if applicable
        if i < len(board) - 1:
            if board[i+1][j] == word[curChar]:
                if self.search(board, i+1, j, word, curChar+1):
                    return True
        # if we've made it down here then none of our searching up,down,left,right worked, return false
        board[i][j] = tmp
        return False