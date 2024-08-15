class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 1:
            return 0
        intervals.sort(key= lambda x: x[1])
        end = intervals[0][1]
        number_of_nonoverlaps = 1
        for interval in intervals[1:]:
            start = interval[0]
            if start >= end:
                number_of_nonoverlaps += 1
                end = interval[1]
        return n - number_of_nonoverlaps
        