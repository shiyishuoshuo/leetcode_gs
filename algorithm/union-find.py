class UnionFind:
    def __init__(self, n) -> None:
        self.size = n
        self.parent = [i for i in range(n)]
        
    def union(self, p: int, q:int) -> None:
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        self.parent[root_p] = root_q
        self.size -= 1
        
    
    def connected(self, p: int, q: int) -> bool:
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q
    
    def find(self, x:int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def count(self) -> int:
        return self.size
    
    
uf = UnionFind(10)
assert uf.count() == 10
uf.union(0, 1)
uf.union(1, 2)
assert uf.connected(0, 2)
assert uf.count() == 8
uf.union(1, 5)
assert uf.connected(5, 2)
assert uf.count() == 7

        
    
    