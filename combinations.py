class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        # driver code for dfs
        for i in range(1, n - k + 2):
            self.dfs(n, k, result, [], i)
        return result
    
    def dfs(self, n, k, result, combo, curNum):
        combo = combo.copy()
        combo.append(curNum)
        # If our current combination has k nums in it, append and return
        if len(combo) == k:
            result.append(combo.copy())
            return
        # otherwise, keep working down the tree making combos
        for i in range(curNum + 1, n+1):
            self.dfs(n, k, result, combo, i)
        return