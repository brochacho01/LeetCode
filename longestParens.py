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
            r1[i+1] = r1[i] + 1
        if s[j] == ')':
            r2[j - 1] = r2[j] + 1