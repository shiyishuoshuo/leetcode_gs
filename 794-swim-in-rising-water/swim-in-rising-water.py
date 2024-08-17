class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float('inf')
        swim_times = [[INF] * n for _ in range(n)]
        swim_times[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        dirs = [(-1, 0),(1, 0),(0, 1),(0, -1)]

        while pq:
            cur_time, cur_x, cur_y = heapq.heappop(pq)
            if cur_x == n - 1 and cur_y == n - 1:
                return cur_time
            if cur_time > swim_times[cur_x][cur_y]:
                continue
            
            for next_x, next_y in dirs:
                new_x, new_y = cur_x + next_x, cur_y + next_y
                if new_x not in range(n) or new_y not in range(n):
                    continue
                new_time = max(cur_time, grid[new_x][new_y])
                if new_time < swim_times[new_x][new_y]:
                    swim_times[new_x][new_y] = new_time
                    heapq.heappush(pq, (new_time, new_x, new_y))
        
        return -1
            
        