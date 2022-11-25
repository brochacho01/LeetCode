class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Iterate over intervals. At each interval check to see if start of or end of newInterval line up with current entry in list. If so, take min and insert, then look at the next interval to see if more merging needs to be done.
        nS = newInterval[0]
        nE = newInterval[1]
        isInserted = False
        # Catch edge case of empty input
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        # Need to check if newInterval is less than start interval
        if nE < intervals[0][0]:
            intervals.insert(0,newInterval)
            return intervals 
        for i in range(len(intervals)):
            # If overlap
            if (nS >= intervals[i][0] and nS <= intervals[i][1]) or (nE >= intervals[i][0] and nE <= intervals[i][1]) or (nS < intervals[i][0] and nE > intervals[i][1]):
                intervals[i][0] = min(nS, intervals[i][0])
                intervals[i][1] = max(nE, intervals[i][1])
                # Need to look ahead and perform merging
                i += 1
                isInserted = True
                # Check to see if tuples after i need to be merged
                while i < len(intervals):
                    # If overlaps with next
                    if intervals[i-1][1] >= intervals[i][0]:
                        # Merge
                        intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                        # Remove merged tuple
                        intervals.remove(intervals[i])
                    else:
                        break
            # Check to see if interval falls between next and prev interval
            elif i < len(intervals) - 1:
                if nS > intervals[i][1] and nE < intervals[i+1][0]:
                    # simply insert interval
                    intervals.insert(i+1, newInterval)
                    isInserted = True
            if isInserted:
                break
        # If we get to here and interval has not been inserted, append to end
        if not isInserted:
            intervals.append(newInterval)
        return intervals