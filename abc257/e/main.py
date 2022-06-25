N = int(input())
C = [0] + list(map(int, input().split()))

dp = [[] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 10):
        if i - C[j] >= 0:
            tmp = dp[i-C[j]][:]
            tmp.append(j)
            dp[i] = max(dp[i], tmp)

print(*dp[N], sep='')
