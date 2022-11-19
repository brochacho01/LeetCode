class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # The issue here is just converting the strings to ints
        # Get the length of each string
        nums = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '0' : 0}
        st1Len = len(num1)
        st2Len = len(num2)
        num1I = 0
        num2I = 0
        for i in range(st1Len):
            num1I = (10 * num1I) + nums.get(num1[i])
        for i in range(st2Len):
            num2I = (10 * num2I) + nums.get(num2[i])
        return str(num1I * num2I)