class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Turn each string into a char array
        # Sort the char array
        # then use the char array as key in a dict with string as value
        # if key already in, add string
        # build up output with all the strings
        sLen = len(strs)
        dc = {}
        for i in range(sLen):
            curList = list(strs[i])
            List.sort(curList)
            # turn List back into string of sorted characters to use as a key
            curStr = str(curList)
            if dc.get(curStr, -1) == -1:
                dc.update({curStr : [strs[i]]})
            else:
                stList = dc.get(curStr)
                stList.append(strs[i])
                dc.update({curStr : stList})
        return dc.values()    