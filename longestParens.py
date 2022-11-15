class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sLen = len(s)
        # Parens will be a 2d list where row 1 represents number open parens up to and including i
        # row 2 represents number close parens after and including i
        parens = []
        # create dp list
        r1 = []
        r2 = []
        # need dp to be 1 longer than s
        for i in range(sLen + 1): 
            r1.append(0)
            r2.append(0)
        parens.append(r1)
        parens.append(r2)
        j = sLen - 1
        # going to have a bug regarding indexing at end of r2
        for i in range(sLen):
            if s[i] == '(':
                parens[0][i+1] = parens[0][i] + 1
            if s[j] == ')':
                parens[1][j] = parens[1][j + 1] + 1
            j -= 1
        # Iterate back over dp array to find index that has greatest val where r1 matches r2
        result = 0
        for i in range(len(parens[0])):
            if parens[0][i] == parens[1][i] and parens[0][i] > result:
                result = parens[0][i]
        return result