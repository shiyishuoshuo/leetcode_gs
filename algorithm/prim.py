import heapq

class Prim:
    def __init__(self, graph:list[list[tuple]]) -> None:
        self.graph = graph
        
    def min_weight(self) -> int:
        n = len(self.graph)
        visited = [False] * n
        visited[0] = True
        min_heap = []
        weighted_sum = 0
        
        def cut(node: int):
            for next_node, weight in self.graph[node]:
                if not visited[next_node]:
                    heapq.heappush(min_heap, (weight, next_node))
        cut(0)
        while min_heap:
            weight, to_node = heapq.heappop(min_heap)
            if visited[to_node]:
                continue
            weighted_sum += weight
            visited[to_node] = True
            cut(to_node)
        return weighted_sum

graph = [[] for _ in range(5)]
graph[0].append((4, 999))
graph[4].append((0, 999))

graph[0].append((1, 5))
graph[1].append((0, 5))

graph[1].append((2, 3))
graph[2].append((1, 3))

graph[3].append((2, 8))
graph[2].append((3, 8))

graph[3].append((4, 7))
graph[4].append((3, 7))

prim = Prim(graph)
print(f'{prim.min_weight()}')
assert prim.min_weight() == 23     
            
            
        