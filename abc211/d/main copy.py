from collections import deque

MOD = 1_000_000_007

N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [0 for i in range(N)]

Q = deque()

if len(G[0]) > 0:
    Q.append([0])
    dist[0] = 1

while len(Q) > 0:
    I = Q.popleft()
    J = []

    for i in I:        
        for j in G[i]:
            dist[j] += 1
            J.append(j)
    
    Q.append(J)
    
    if dist[N-1] > 0:
        break

print(dist[N-1] % MOD)
