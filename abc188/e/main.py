N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = A.copy()
edges = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    edges[y].append(x)
ans = -10**18
for i in range(1, N+1):
    for x in edges[i]:
        ans = max(ans, A[i] - dp[x])
        dp[i] = min(dp[i], dp[x])
print(ans)
