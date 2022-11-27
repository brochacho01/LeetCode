class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Iterate through the list. Each time when a new word is encountered, leave a pointer at its first character until another word is found. Although with python we can interate backwards to be even faster
        firstChar = -1
        lastChar = -1
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha() and lastChar == -1:
                lastChar = i+1
            if s[i] == ' ' and lastChar != -1:
                firstChar = i + 1
                break
        # Need to do a check just in case there are no spaces
        if firstChar == -1:
            firstChar = 0
        return lastChar - firstChar