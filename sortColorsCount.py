class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use list.count method for this
        # list.count method is faster than iterating over list and manually counting
        num0 = nums.count(0)
        num1 = nums.count(1) + num0
        for i in range(len(nums)):
            if i < num0:
                nums[i] = 0
            elif i < num1:
                nums[i] = 1
            else:
                nums[i] = 2