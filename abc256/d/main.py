import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n: int, LR) -> None:
        self.parents = [-1] * n
        self.data = [(LR[i][1], LR[i][2]) for i in range(n)]

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
        self.data[x] = (min(self.data[x][0], self.data[y][0]), max(self.data[x][1], self.data[y][1]))
        pass

N = int(input())
LR = []
for i in range(N):
    l, r = map(int, input().split())
    LR.append((i, l, r))

uf = UnionFind(N, LR)

# Lが小さい順にソート
LR.sort(key=lambda x: (x[1], -x[2]))

lastI = -1
maxR = -1
for i, l, r in LR:
    if l <= maxR:
        uf.union(i, lastI)
    maxR = max(maxR, r)
    lastI = i

ans = []
for i in range(N):
    if uf.parents[i] < 0:
        ans.append(uf.data[i])
ans.sort()
for a in ans:
    print(*a)
