N = int(input())
MOD = 998244353
dp = [1] * 11
dp[0] = 0
dp[10] = 0
for i in range(N-1):
    prev = dp[::]
    for j in range(1, 10):
        dp[j] = (prev[j-1] + prev[j] + prev[j+1]) % MOD
print(sum(dp) % MOD)