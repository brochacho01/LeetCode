# Current issue is that there's multiple possible starts that overlap
def strStr(haystack, needle):
    shift = int(0)
    # Do shift method
    while shift < len(haystack) - len(needle) + 1:
        # Check to see if we've found starting character
        if haystack[shift] == needle[0]:
            # Iterate over rest of substring to check for equality
            j = shift
            matched = int(0)
            for curMatch in range(len(needle)):
                # If we've found matching character, increment and continue
                if haystack[j] == needle[matched]:
                    matched += 1
                # If no match, break out
                else:
                    break
                j += 1
            # Once done iterating over substring if numbers matched is == length, then we've matched all characters in needle so we return our shift
            if matched == len(needle):
                return shift
        shift += 1
    return -1
        