class Solution:
    # hHash can be improved by calculating moving window instead of redoing window
    def strStr(self, haystack: str, needle: str) -> int:
        # Do hashing method
        # First hash needle
        nLen = len(needle)
        nHash = 0
        for i in range(nLen):
            nHash += ord(needle[i])
        # need to hash each substring of haystack
        hLen = len(haystack)
        hHash = {}
        winHash = 0
        if nLen > hLen:
            return -1
        # calculate first window then move window
        for i in range(0, nLen):
            winHash += ord(haystack[i])
        # add first hash entry
        c1 = []
        c1.append(0)
        hHash.update({winHash : c1})
        winHash -= ord(haystack[0])
        for i in range(nLen, hLen):
            winHash += ord(haystack[i])
            if(hHash.get(winHash, -1) == -1):
                coord = []
                coord.append(i - nLen + 1)
                hHash.update({winHash : coord})
            else:
                coord = hHash.get(winHash)
                coord.append(i - nLen + 1)
                hHash.update({winHash : coord})
            # Need to substract first val in window
            winHash -= ord(haystack[i - nLen + 1])
        
        
        # Evaluate nHash vs hHash
        coords = []
        if hHash.get(nHash, -1) == -1:
            return -1
        else:
            coords = hHash.get(nHash)
        cLen = len(coords)
        for i in range(cLen):
            index = 0
            start = coords[i]
            flag = 1
            for j in range(start, start + nLen):
                if needle[index] != haystack[j]:
                    flag = 0
                    break
                index += 1
            if flag == 1:
                return start
        return -1
