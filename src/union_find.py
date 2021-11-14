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
