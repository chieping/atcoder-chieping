
from collections import defaultdict

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n
        self.data = [0] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.union_hook(x, y)

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def group_count(self):
        return len(self.roots())
            
    def union_hook(self, x, y):
        pass


N, M = map(int, input().split())
res = [0]
AB = defaultdict(list)
uf = UnionFind(N+1)

for i in range(M):
    a, b = map(int, input().split())
    AB[min(a, b)].append((a, b))

ans = 0
for n in range(N, 1, -1):
    ans += 1
    for a, b in AB[n]:
        if not uf.same(a, b):
            ans -= 1
        uf.union(a, b)
    res.append(ans)

print(*res[::-1], sep='\n')
