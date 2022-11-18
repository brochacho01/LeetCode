class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Time to take binary approach, can do this because list is sorted in ascending order
        nLen = len(nums)
        result = []
        if nLen == 1:
            if nums[0] == target:
                result.append(0)
                result.append(0)
                return result
        low = 0
        high = nLen - 1
        while low <= high:
            mid = (low + high) // 2
            # mid has plopped us in target
            if nums[mid] == target:
                # Need to find start, finish
                start = mid - 1
                # Find first digit that doesn't match target, start += 1 of first non digit
                while start >= 0 and nums[start] == target:
                    start -= 1
                start += 1
                end = mid + 1
                while end <= nLen - 1 and nums[end] == target:
                    end += 1
                end -= 1
                result.append(start)
                result.append(end)
                return result
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        result.append(-1)
        result.append(-1)
        return result