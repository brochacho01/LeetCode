def longestPalindrome(self, s: str) -> str:
        # Variation on countSubstrings
        longestStart = -1
        longestEnd = -1
        # Important that this is initialized to -1 because otherwise s of size 1 will give wrong output because right - left = 0 and miss
        longestLength = -1
        sLen = len(s)
        for i in range(sLen):
            left = i
            right = i
            while left >= 0 and right < sLen and s[left] == s[right]:
                if right - left > longestLength:
                    longestLength = right - left
                    longestStart = left
                    longestEnd = right
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < sLen and s[left] == s[right]:
                if right - left > longestLength:
                    longestLength = right - left
                    longestStart = left
                    longestEnd = right
                left -= 1
                right += 1
        longestPalin = s[longestStart:longestEnd + 1]
        return longestPalin