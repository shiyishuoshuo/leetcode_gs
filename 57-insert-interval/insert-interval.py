class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        interval_len = len(intervals)
        left, right = 0, interval_len
        insert_start, insert_end = newInterval[0], newInterval[1]
        while left < right:
            mid = (right - left) // 2 + left
            if intervals[mid][0] >= insert_start:
                right = mid
            else:
                left = mid + 1

        intervals.insert(left, newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


        
        