# 解説AC
# 最小全域木 クラスカル法
# 辺をコストの低い順に並べ、辺を張ることで連結になる
# 場合は辺を張るということを繰り返す
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
Xsort = []
Ysort = []
for i in range(N):
    x, y = map(int, input().split())
    Xsort.append((x, i))
    Ysort.append((y, i))
Xsort.sort()
Ysort.sort()

# cost, u, v
edge = []

for i in range(N-1):
    x1, j = Xsort[i]
    x2, k = Xsort[i+1]
    edge.append((x2-x1, j, k))
for i in range(N-1):
    y1, j = Ysort[i]
    y2, k = Ysort[i+1]
    edge.append((y2-y1, j, k))
edge.sort()

parent = [-1] * N

def unite(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if parent[a] < parent[b]:
        a, b = b, a
    parent[a] += parent[b]
    parent[b] = a

def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def same(a, b):
    return find(a) == find(b)

ans = 0
for cost, u, v in edge:
    if not same(u, v):
        unite(u, v)
        ans += cost
print(ans)