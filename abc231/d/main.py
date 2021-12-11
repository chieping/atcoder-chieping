class UnionFind:
    def __init__(self, n: int) -> None:
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

    def union_hook(self, x, y):
        pass


N, M = map(int, input().split())
uf = UnionFind(N+1)
cnt = [0] * (N+1)

def fail():
    print('No')
    exit()

for i in range(M):
    a, b = map(int, input().split())

    if uf.same(a, b):
        fail()
    uf.union(a, b)
    cnt[a] += 1
    cnt[b] += 1

if max(cnt) > 2:
    fail()
else:
    print('Yes')
