class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        start_index, end_index = 0, 0
        count = 0
        res = 0

        while start_index < len(intervals):
            if start[start_index] < end[end_index]:
                count += 1
                start_index += 1
            else :
                count -= 1
                end_index += 1

            res = max(count, res)

        return res
        