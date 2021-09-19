from collections import defaultdict
INF = 10**18
N = int(input())
X, Y = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]

# dp[i][j][k] = 最小の弁当個数
dp = [[[INF] * (Y+1) for i in range(X+1)] for i in range(N+1)]

dp[0][0][0] = 0

for i in range(1, N + 1):
    tako = B[i-1][0]
    tai = B[i-1][1]
    for j in range(X+1):
        for k in range(Y+1):
            # 買う場合
            dp[i][min(j + tako, X)][min(k + tai, Y)] = min(dp[i][min(j + tako, X)][min(k + tai, Y)], dp[i-1][j][k] + 1)
            # 買わない場合
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])

if dp[N][X][Y] != INF:
    print(dp[N][X][Y])
else:
    print(-1)
