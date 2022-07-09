import sys
input = sys.stdin.readline
N = int(input())
sx, sy, tx, ty = map(int, input().split())

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

uf = UnionFind(N)

X = []
Y = []
R = []

start = -1
end = -1

for i in range(N):
    x, y, r = map(int, input().split())
    distS = ((sx-x)**2 + (sy-y)**2)
    distT = ((tx-x)**2 + (ty-y)**2)
    if distS == r*r:
        start = i
    if distT == r*r:
        end = i

    X.append(x)
    Y.append(y)
    R.append(r)

for i in range(N):
    for j in range(i+1, N):
        dist = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)
        if dist > (R[i] + R[j])**2: continue
        if dist < (R[i] - R[j])**2 or dist < (R[j] - R[i])**2: continue
        uf.union(i, j)

print('Yes' if uf.same(start, end) else 'No')
