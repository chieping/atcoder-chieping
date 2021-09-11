import sys
sys.path.append('../../')
from src.union_find import UnionFind

N, M = map(int, input().split())

V = [list(map(int, input().split())) for i in range(M)]
V.sort(key=lambda x: x[2])

uf = UnionFind(N)

ans = 0

for a, b, c in V:
    a, b = a - 1, b - 1
    if uf.find(a) == uf.find(b):
        if c > 0:
            ans += c
        continue
    uf.unite(a, b)

print(ans)

