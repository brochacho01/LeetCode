def countSubstrings(self, s: str) -> int:
    palins = 0
    sLen = len(s)
    # Iterate over the entire string
    for i in range(sLen):
        # Count number of odd length palindromes, starting at point i
        left = i
        right = i
        # Go outwards from starting point in both directions calculating odd length palindromes
        while left >= 0 and right < sLen and s[left] == s[right]:
            palins += 1
            left -= 1
            right += 1
        # Now calculate even length palindromes from starting point
        left = i
        right = i + 1
        while left >= 0 and right < sLen and s[left] == s[right]:
            palins += 1
            left -= 1
            right += 1
    return palins