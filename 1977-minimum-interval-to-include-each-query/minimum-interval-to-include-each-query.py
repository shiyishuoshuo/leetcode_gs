class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        interval_index = 0
        res = defaultdict(int)

        for q in sorted(queries):
            while interval_index < len(intervals) and intervals[interval_index][0] <= q:
                start, end = intervals[interval_index]
                heapq.heappush(minHeap, (end - start + 1, end))
                interval_index += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]

        