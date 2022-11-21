class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if target > nums[low]:
            return low + 1
        else:
            return low