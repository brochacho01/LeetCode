# https://leetcode.com/problems/divide-two-integers/

# Currently doesn't account for negative divisors
def divide(self, dividend: int, divisor: int) -> int:
    numDivs = int(0)
    div = int(0)
    negsorFlag = 1
    negdendFlag = 1
    if divisor < 0:
        divisor = abs(divisor)
        negsorFlag = -1
    if dividend < 0:
        dividend = abs(dividend)
        negdentFlag = -1
    while div <= dividend:
        div += divisor
        numDivs += 1
    div -= divisor
    numDivs -= 1
    # Need to flip sign
    if (negsorFlag < 0 and negdendFlag > 0) or (negsorFlag > 0 and negdendFlag < 0):
        temp = numDivs
        numDivs -= numDivs
        numDivs -= temp
    return numDivs