#Recursive approach
def lengthOfLongestSubstring(self, s):
    maxLen = int(0)
    #create start index and end index of sbustring
    start = int(0)
    end = int(0)
    curLen = int(0)
    #dict to track characters in current substring
    curChars = dict()
    for end in range(len(s)):
        #Check for repeat
        if curChars.get(s[end], -1) != -1:
            #found repeat char, time for new substring
            if curLen > maxLen:
                maxLen = curLen
            #Need to move start forward to exclude repeat char
            start = curChars.get(s[end]) + 1
            
            #Need to update curChars for cleared characters
            curChars.clear()
            for i in range(start, end + 1):
                curChars.update({s[i] : i})
            #Need to adjust curLen based on how the start index moved
            curLen = len(curChars.keys())
        else :
        # Still unique character in substring, add 1 to length, add char to dict to track
            curLen += 1
            curChars.update({s[end] : end})
        # want to increment end each time
    if curLen > maxLen:
        maxLen = curLen
    return maxLen

def main():
    # s = "abcabbacb"
    # s = "pwwkew"
    # s = "au"
    # s = " "
    s = "dvdf"
    print(lengthOfLongestSubstring(None, s))

if __name__ == "__main__":
    main()