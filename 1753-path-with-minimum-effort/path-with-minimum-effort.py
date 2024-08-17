class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        INF = float('inf')
        efforts = [[INF] * col for _ in range(row)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        dirs = [(-1, 0),(1, 0),(0, 1),(0, -1)]

        while pq:
            effort, cur_x, cur_y = heapq.heappop(pq)
            if cur_x == row - 1 and cur_y == col - 1:
                return effort
            if effort < efforts[cur_x][cur_y]:
                continue
            
            for x , y in dirs:
                new_x, new_y = x + cur_x, cur_y + y
                if new_x not in range(row) or new_y not in range(col):
                    continue
                max_effort = max(effort, abs(heights[new_x][new_y] - heights[cur_x][cur_y]))
                if max_effort < efforts[new_x][new_y]:
                    efforts[new_x][new_y] = max_effort
                    heapq.heappush(pq, (max_effort, new_x, new_y))

        return 0