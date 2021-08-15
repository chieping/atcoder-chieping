from collections import deque

N, M = map(int, input().split())
edges = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

S = int(input())
S -= 1
K = int(input())
T = list(map(lambda x: int(x) - 1, input().split()))
T.append(S)

# Dist[k: 頂点T[k]から][l: 頂点T[l]までの] = 移動コスト
Dist = []
for t1 in T:
    INF = 10**100
    dist = [INF] * N
    que = deque()
    que.append(t1)
    dist[t1] = 0
    while len(que) > 0:
        i = que.popleft()
        for j in edges[i]:
            if dist[j] == INF:
                dist[j] = dist[i] + 1
                que.append(j)
    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)

# 巡回セールスマン問題
# cost[n: Tの中で訪れた頂点の集合][i: 最後にいる頂点] = コスト最小値
ALL = 1<<K
cost = [[INF] * K for i in range(ALL)]

for i in range(K):
    cost[1<<i][i] = Dist[K][i]

def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(K):
        for j in range(K):
            if has_bit(n, j) or i == j:
                continue
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + Dist[i][j])

print(min(cost[ALL-1]))
