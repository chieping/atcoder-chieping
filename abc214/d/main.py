class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]


N = int(input())
es = []

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    es.append((w, u, v))
es.sort()

uf = UnionFind(N)

ans = 0

for w, a, b in es:
    ans += w * uf.size(a) * uf.size(b)
    uf.unite(a, b)

print(ans)
