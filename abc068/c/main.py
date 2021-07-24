from collections import deque


N, M = map(int, input().split())

G = [[] for i in range(N)]

for _ in range(M):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    G[ai].append(bi)
    G[bi].append(ai)

dist = [-1 for i in range(N)]

Q = deque()

Q.append(0)

dist[0] = 0

while len(Q) > 0:
    i = Q.popleft()

    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)

if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
        
