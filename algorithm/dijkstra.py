import heapq

class Dijkatra:
    def __init__(self, graph: list[list[tuple]]) -> None:
        self.graph = graph
        
    def min_weight(self, start: int) -> list[int]:
        INF = float('inf')
        size = len(self.graph)
        distances = [INF] * size
        distances[start] = 0
        min_heap = [(start, 0)]
        
        while min_heap:
            cur_node, cur_distance = heapq.heappop(min_heap)
            for next_node, next_distance in self.graph[cur_node]:
                new_distance = next_distance + cur_distance
                if distances[next_node] > new_distance:
                    distances[next_node] = new_distance
                    heapq.heappush(min_heap, (next_node, new_distance))
        return distances
    
graph = [[] for _ in range(6)]
graph[0].append((4, 5))
graph[0].append((3, 8))
graph[0].append((1, 9))
graph[1].append((2, 2))
graph[2].append((5, 1))
graph[3].append((5, 2))
graph[4].append((5, 6))

shortest_path = Dijkatra(graph)
print(f'{shortest_path.min_weight(0)}')
assert shortest_path.min_weight(0)[5] == 10

min_heap = []
heapq.heappush(min_heap, (10, 5))
heapq.heappush(min_heap, (8, 1))
heapq.heappush(min_heap, (6, 2))
heapq.heappush(min_heap, (3, 3))

while min_heap:
    print(f'{heapq.heappop(min_heap)}')
                
        