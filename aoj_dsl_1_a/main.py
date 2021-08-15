import sys
sys.setrecursionlimit(10**6)

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [-1] * n
        self.ranks = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.parents[x] = y

n, q = map(int, input().split())
uf = UnionFind(n)
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        uf.unite(x, y)
    else:
        if uf.find(x) == uf.find(y):
            print(1)
        else:
            print(0)
