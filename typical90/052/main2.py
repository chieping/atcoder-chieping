from sys import stdin
N = int(stdin.readline())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
MOD = 10**9+7
dp = [0] * 6
dp[0] = 1

for i in range(N):
    next = [0] * 6
    for j in range(6):
        next[j] = (sum(dp) * A[i][j]) % MOD
    dp = next

print(sum(dp) % MOD)
