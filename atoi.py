def myAtoi(self, s: str) -> int:
    sLen = len(s)
    if sLen == 0:
        return 0
    # read in whitespace
    start = 0
    sign = 1
    end = 0
    for i in range(sLen):
        if s[i] == ' ':
            start += 1
        else:
            break
    # Look for +/-
    if s[i] == '-':
        sign = -1
        start += 1
    elif s[i] == '+':
        start += 1
    # Now begin reading in digits
    digStr = ""
    for i in range(start, sLen):
        if str(s[i]).isdigit():
            digStr += s[i]
        else:
            end = i
            break
    # Check to see if digits were read in
    digLen = len(digStr)
    if digLen == 0:
        # Need to return +/- 0
        if sign == 1:
            return 0
        else:
            return -0
    # Now begin constructing int
    power = 10**(digLen - 1)
    result = int(0)
    for i in range(digLen):
        result += int(int(digStr[i]) * power)
        power /= 10
    if sign == -1:
        result *= -1
    # Now check to see if in bounds of 32bit int
    if result > (2**31) -1:
        return (2**31) -1
    elif result < -2**31:
        return -2**31
    else:
        return result