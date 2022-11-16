class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Could brute force generate all, then validate
        result = []
        self.parens("(", 1, n,  n-1, n, result)
        return result

    def parens(self, str, numP, n, numO, numC, result):
        # This if doesn't work
        print(numP)
        if numP//2 == n and numO == 0 and numC == 0:
            if self.validate(str):
                result.append(str)
                return
        else:
            if numO > 0:
                self.parens(str + "(", numP + 1, n, numO - 1, numC, result)
            if numC > 0:
                self.parens(str + ")", numP + 1, n, numO, numC - 1, result)
        return

    def validate(self, str):
        numO = 0
        for i in range(len(str)):
            if str[i] == '(':
                numO += 1
            else:
                numO -= 1
            if numO < 0:
                return False
        if numO == 0:
            return True
        else:
            return False