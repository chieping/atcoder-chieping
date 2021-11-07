class UnionFind:
    def __init__(self, n: int) -> None:
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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


MOD = 998244353
N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.unite(u, v)

ans = 1

for root in uf.roots():
    if uf.size(root)>2:
        ans *= 2
        ans %= MOD
    else:
        ans *= 0

print(ans)
