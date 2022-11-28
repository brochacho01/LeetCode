class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Idea is to iterate over the string. Add each number from the string to the stack. During this, we want to remove the highest value most significant digits. To do this, at each element of the string, we want to see if it's less than the top element of the stack while we still have digits to remove. If so, we should pop the stack then append curString number. At the end if we still have any digits to remove, remove any leading digits then remove leading zeros
        stack = []
        # fast check for edge cases
        if len(num) <= k:
            return "0"
        # Iterate over the string
        for i in range(len(num)):
            # Check to see if we have digits to remove and items in the stack
            while k > 0 and stack:
                # If curNum is greater than top of stack, pop num off stack and decrement k
                if ord(stack[-1]) > ord(num[i]):
                    stack.pop()
                    k -= 1
                # If we don't need to pop, leave loop
                else:
                    break
            # Always when we're done, append current number to the stack
            stack.append(num[i])
        # There's a chance that we still have digits to remove, if so, pop top items off stack as they should be greater than previous items in stack due to the increasing structure
        while k > 0 and stack:
            stack.pop()
            k -= 1
        # Need to remove any leading zeros
        while stack:
            if stack[0] == "0":
                stack.pop(0)
            else:
                break
        if len(stack) == 0:
            return "0"
        return ''.join(stack)