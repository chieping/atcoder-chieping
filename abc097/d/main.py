from collections import defaultdict

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [-1] * n
        self.data = [0] * n
        self.n = n

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
    
    def groups(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def union_hook(self, x, y):
        pass


N, M = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
X = [0] * M
Y = [0] * M
for i in range(M):
    X[i], Y[i] = map(lambda x: int(x)-1, input().split())
uf = UnionFind(N)
for x, y in zip(X, Y):
    uf.union(x, y)
ans = 0
for group in uf.groups().values():
    q = {P[g] for g in group}
    ans += len(q.intersection(group))
print(ans)
