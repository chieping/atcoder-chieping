from collections import defaultdict, deque

MOD = 1_000_000_007

N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [0 for i in range(N)]
visited = [False] * N

Q = deque()

if len(G[0]) > 0:
    Q.append({ 0: 1})
    dist[0] = 1
    visited[0] = True

while len(Q) > 0:
    I = Q.popleft()
    J = defaultdict(int)

    for i, v in I.items():
        for j in G[i]:
            if not visited[j]:                
                dist[j] = (dist[j] + v) % MOD
                J[j] += v

    for i, v in J.items():
        visited[i] = True
    
    Q.append(J)
    
    if dist[N-1] > 0:
        break

print(dist[N-1])
