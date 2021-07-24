MOD = 1_000_000_007
N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [None] * N
Q = [0]
cnt = [0] * N

dist[0] = 0
cnt[0] = 1

for v in Q:
    for vv in G[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            Q.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            cnt[vv] %= MOD

print(cnt[N-1])
