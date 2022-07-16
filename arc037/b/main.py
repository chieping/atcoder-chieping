N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)

visited = [False] * N

def dfs(now, prev=-1):
    if visited[now]:
        return 0
    visited[now] = True
    ret = 1
    for i in edge[now]:
        if i == prev: continue
        ret &= dfs(i, now)
    return ret

ans = 0
for i in range(N):
    if not visited[i]:
        ans += dfs(i)
print(ans)
