class Solution:
    def longestValidParentheses(self, s: str) -> int:
        numO = 0
        numC = 0
        curMax = 0
        # Iterate from front to back looking at valid substrings
        # Once more close than open have been read, current substring is invalid, check against max and update if needed
        sLen = len(s)
        for i in range(sLen):
            # Check char, increment
            if s[i] == '(':
                numO += 1
            else:
                numC +=1
            # If numO and numC are equal, we have a valid substring, check against max and update as necessary
            if numO == numC:
                curMax = max(curMax, numO + numC)
            # if numO < numC, we've found more close than open in this substring, therefore current substring is invalid, reset vals
            elif numO < numC:
                numO = 0
                numC = 0
        numO = 0
        numC = 0
        # Need to iterate back to front, because if upon first iteration there is always more open than close but there exists a valid substring, then the max will not get updated. But when evaluating based on closed parens this will catch it. First loop does this but visa versa
        for i in range(sLen -1, -1, -1):
            if s[i] == '(':
                numO += 1
            else:
                numC += 1
            if numO == numC:
                curMax = max(curMax, numO + numC)
            elif numO > numC:
                numO = 0
                numC = 0
        return curMax



def main():
    print("Hello")

if __name__ == "__main__":
    main()