from collections import deque
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append(b)
ans = 0
for n in range(N):
    Q = deque()
    visited = [False] * N
    visited[n] = True
    ans += 1
    Q.append(n)
    while len(Q) > 0:
        a = Q.pop()
        for b in edges[a]:
            if not visited[b]:
                visited[b] = True
                Q.append(b)
                ans += 1
print(ans)
