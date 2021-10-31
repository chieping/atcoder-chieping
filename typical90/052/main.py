N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
MOD = 10**9+7
# dp[i: i個目のサイコロまで処理したときの][j: 最後に出た目がjのとき] = そのときの出目の総和
dp = [[0] * 6 for i in range(N+1)]
dp[0] = [1, 0, 0, 0, 0, 0]

for i in range(1, N+1):
    souwa = sum(dp[i-1])
    for j in range(6):
        dp[i][j] = (souwa * A[i-1][j]) % MOD

print(sum(dp[N]) % MOD)
