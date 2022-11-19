class Solution:
    def myPow(self, x: float, n: int) -> float:
        # corner case where n == 0, return 1
        if n == 0:
            return x / x
        # If power is negative then it's (1/num)^n
        if n < 0:
            x = 1 / x
            n = abs(n)
        # Now enter loop
        # Loop version too slow, I wrongly assumed I couldn't use **
        x = x ** n
        # base = x
        # for i in range(1, n):
        #     x *= base
        return x