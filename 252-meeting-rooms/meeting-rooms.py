class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 0:
            return True

        intervals.sort(key = lambda x: x[0])

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
                continue
            return False
        
        return True
            


        