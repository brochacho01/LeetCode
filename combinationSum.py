# NOTE for python: when you add a listA to listB and then later change listA, it changes in listB as well. make a copy of listA then add to listB
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Do a sort here because it allows us to impose some rules during backtracking
        candidates.sort()
        cLen = len(candidates)
        ans = []
        for i in range(cLen):
            self.backtrack(candidates, i, [], target, 0, ans)
        return ans
    
    # When a backtrack occurs, need to pop element off of curList
    def backtrack(self,candidates, curI, curList, target, curSum, ans):
        # Add curI value to curSum, then check to see if invalid
        if curI == len(candidates):
            return
        curSum += candidates[curI]
        curList.append(candidates[curI])
        # if Invalid. We don't have to worry about checking curI + 1 because it will always be greater than curI due to sort
        if curSum > target:
            curList.pop()
            return
        # Check if target
        elif curSum == target:
            # If so, append a copy of curList to answer
            ans.append(curList.copy())
            curList.pop()
            return
        # If not invalid or not target, need to keep checking combinations
        # Check adding another value of itself
        self.backtrack(candidates, curI, curList, target, curSum, ans)
        # Check adding any one of the other values in candidates
        for i in range(curI + 1, len(candidates)):
            self.backtrack(candidates, i, curList, target, curSum, ans)
        curList.pop()
        return
