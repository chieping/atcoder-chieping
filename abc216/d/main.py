from collections import deque


N, M = map(int, input().split())

G = [[] for i in range(M)]
U = [-1] * (N + 1)

for i in range(M):
    k = int(input())
    G[i] = deque(list(map(int, input().split())))

Q = deque()
for i in range(M):
    Q.append((G[i][0], i))

while len(Q) > 0:
    n, i = Q.pop()

    if U[n] != -1:
        j = U[n]
        G[i].popleft()
        G[j].popleft()
        if len(G[i]) > 0:
            Q.append((G[i][0], i))
        if len(G[j]) > 0:
            Q.append((G[j][0], j))
    else:
        U[n] = i

ans = 'Yes'
for i in range(M):
    if len(G[i]) > 0:
        ans = 'No'
print(ans)
