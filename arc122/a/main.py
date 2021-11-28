N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

ans_plus = 0
ans_minus = 0

# dp[i: i個の+-を並べ、][j: 最初が+なら0, -なら1] = 場合の数
dp = [[0, 1] for i in range(N)]

dp[0][0] = 0
dp[0][1] = 0
if N == 1:
    print(A[0])
    exit()

dp[1][0] = 1
dp[1][1] = 1
ans_plus += A[-1]
ans_minus -= A[-1]

for i in range(2, N):
    ans_minus_tmp = ans_minus
    dp[i][1] = dp[i-1][0]
    ans_minus = ans_plus - A[-i]*dp[i][1]
    ans_minus %= MOD
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][0] %= MOD
    ans_plus = ans_plus + ans_minus_tmp + A[-i]*dp[i][0]
    ans_plus %= MOD

ans_minus += A[0]*dp[N-1][1]
ans_plus += A[0]*dp[N-1][0]

print((ans_plus + ans_minus) % MOD)
