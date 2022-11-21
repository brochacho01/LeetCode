class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # An interval overlaps if start >= curOutputStart and start <= curOutputEnd or end >= curOutputStart and end <= curOutputEnd
        # Problem becomes much easier if intervals are sorted
        list.sort(intervals)
        output = []
        output.append(intervals[0])
        # Need to track current interval in output
        outI = 0
        # Now that intervals are sorted, for each item in intervals, look ahead and begin performing recurrence
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            # If intervals are found to overlap, merge
            if (start >= output[outI][0] and start <= output[outI][1]) or (end >= output[outI][0] and end <= output[outI][1]):
                output[outI][0] = min(start, output[outI][0])
                output[outI][1] = max(end, output[outI][1])
            # If intervals not found to match, append current interval to output and move tracker to the index of curInterval in output
            # We can do this because we sorted intervals, therefore no future interval can overlap with a previous output interval
            else:
                output.append(intervals[i])
                outI += 1
        return output