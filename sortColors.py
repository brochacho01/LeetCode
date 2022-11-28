class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 is red
        # 1 is white
        # 2 is blue
        # could use pointers to track end indices of 0 1 2
        # The idea is that initialize pointers of 0 1 2 to -1
        # Then begin iterating over the list
        # When a color is encountered, if its prev pointer is uninitialized, initialize it to 0
        # Otherwise, move every digit in range of prev num pointer forward 1 then place num at pointer
        # Once val is placed only update myPtr and subsequent ptrs
        # Not guranteed for every color to be in list so we can't pre-initialize variables
        # Only need to sort 0's and 1's because by doing so 2's will get pushed to the back
        rPtr = -1
        wPtr = -1
        for i in range(len(nums)):
            # if red
            if nums[i] == 0:
                # shift everything from rPtr to i forward by one
                for j in range(i, rPtr, -1):
                    nums[j] = nums[j - 1]
                # Place num, need to do plus here because python accepts -1 as an index
                rPtr += 1
                nums[rPtr] = 0
                # Update ptr
                wPtr = rPtr + 1
            # if white
            elif nums[i] == 1:
                # if ptr is not initialized
                if wPtr == -1:
                    wPtr = rPtr + 1
                # Do shifting
                for j in range(i, wPtr, -1):
                    nums[j] = nums[j - 1]
                nums[wPtr] = 1
                wPtr += 1
            # Don't necessarily worry about 2's as they will automatically get pushed to back
        return