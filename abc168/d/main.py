from collections import deque
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

ans = [-1] * (N+1)
Q = deque()
Q.append(1)
while len(Q) > 0:
    now = Q.popleft()
    for nxt in edges[now]:
        if ans[nxt] == -1:
            ans[nxt] = now
            Q.append(nxt)
print('Yes')
print(*ans[2:], sep='\n')
