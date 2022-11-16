# https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Use a dfs style but be smarter than brute force because there is a pattern we can follow
        def dfs(left, right, s):
            # Base case
            if len(s) == n * 2:
                result.append(s)
                return
            # We know the pattern for parenthesis. and we know number of pairs required
            # One left represents one pair, so if we have less left than n, we can add an open parens
            if left < n:
                dfs(left + 1, right, s + '(')
            # We know that for each open parens we need a close, but we can't have more close than open, so if we have more open, add a close
            if right < left:
                dfs(left, right + 1, s + ')')
            result = []
            dfs(0,0, '')
            return result