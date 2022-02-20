import sys
readline = sys.stdin.readline
N, X = map(int, readline().split())
dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    a, b = map(int, readline().split())
    for j in range(X+1):
        if j-a >= 0 and dp[i-1][j-a]:
            dp[i][j] = True
        if j-b >= 0 and dp[i-1][j-b]:
            dp[i][j] = True

print('Yes' if dp[N][X] else 'No')
