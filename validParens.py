class Solution:
    def isValid(self, s: str) -> bool:
        totalP = 0
        totalBc = 0
        totalBk = 0
        lastO = []
        # Need a stack to store last open
        for i in range(len(s)):
            # Open character
            if s[i] == '(':
                totalP += 1
                lastO.append('(')
            elif s[i] == '{':
                totalBc += 1
                lastO.append('{')
            elif s[i] == '[':
                totalBk += 1
                lastO.append('[')
            # Close character
            elif len(lastO) > 0:
                if s[i] == ')' and lastO.pop() == '(':
                    totalP -= 1
                elif s[i] == '}' and lastO.pop() == '{':
                    totalBc -= 1
                elif s[i] == ']' and lastO.pop() == '[':
                    totalBk -= 1
                else:
                    return False
            else:
                return False
        if totalP == 0 and totalBc == 0 and totalBk == 0:
            return True
        else:
            return False