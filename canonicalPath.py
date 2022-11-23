class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        pLen = len(path)
        # want to search for directories to add to stack, or .. to pop item off stack
        while i < pLen:
            # skip past slashes
            if path[i] == '/':
                while i < pLen:
                    if path[i] == '/':
                        i += 1
                    else:
                        break
            elif path[i] == '.':
                # need to see how many dots
                start = i
                isName = False
                while i < pLen:
                    # Here we are reading in a possible command or dirName, read until next / then evaluate
                    if path[i] != '/':
                        if path[i].isalpha() or path[i].isdigit():
                            isName = True
                        i += 1
                    else:
                        break
                numDots = i - start
                # check if two dots
                if numDots == 2 and not isName:
                    # Normally pop item, but first check if stack is empty, otherwise, serves as a no-op
                    if len(stack) != 0:
                        stack.pop()
                # Check if more than one dots, treat as dirName
                elif numDots >= 2:
                    stack.append(path[start:i])
                # Don't do anything for single dot, treat as no-op
            # Otherwise we are at a dirname, need to get full name, then add to stack
            else:
                # If we get to here, we are reading in a dirName
                start = i
                while i < pLen:
                    if path[i] != '/':
                        i += 1
                    else:
                        break
                # Here we have gathered full name, add to stack
                stack.append(path[start:i])
        # Now that we're here we need to build up our answer out of the stack
        result = "/"
        sLen = len(stack)
        for i in range(sLen - 1):
            result += stack[i]
            result += '/'
        # Add last item on without /
        if sLen > 0:
            result += stack[len(stack) - 1]
        return result