from sys import stdin
H, W = map(int, stdin.readline().split())
S = [list(stdin.readline()[:-1]) for _ in range(H)]
MOD = 10**9+7
dp = [[0] * W for _ in range(H)]
X = [[0] * W for _ in range(H)]
Y = [[0] * W for _ in range(H)]
Z = [[0] * W for _ in range(H)]

dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        if S[i][j] == '#':
            continue
        if j > 0:
            X[i][j] = (X[i][j-1] + dp[i][j-1]) % MOD
        if i > 0:
            Y[i][j] = (Y[i-1][j] + dp[i-1][j]) % MOD
        if i > 0 and j > 0:
            Z[i][j] = (Z[i-1][j-1] + dp[i-1][j-1]) % MOD
        dp[i][j] = (X[i][j] + Y[i][j] + Z[i][j]) % MOD

print(dp[H-1][W-1])
