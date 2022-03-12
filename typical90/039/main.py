import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

# その頂点を根とした部分木の大きさを計算する
size = [0] * N

def dfs(i, last = -1):
    size[i] += 1
    for v in edges[i]:
        if v == last:
            continue
        dfs(v, i)
        size[i] += size[v]

dfs(0)

# ある辺に注目し、その辺を取って2つの部分木に分けて見たときに、
# 一方のいずれかの頂点から、もう一方のいずれかの頂点に行くときには、
# その注目している辺を必ず通る。
# よって、その注目している辺が使われる回数は、部分木1のサイズ*部分木2のサイズ となる
# 求める答えは、それぞれの頂点が部分木だった場合の↑を考えて合計したものになる。

ans = 0
for i in range(N):
    ans += size[i] * (N-size[i])

print(ans)
