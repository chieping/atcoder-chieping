K = int(input())
if K % 9:
    print(0)
    exit()

MOD = 10**9+7
dp = [0] * (K+1)
dp[0] = 1

for i in range(K+1):
    for j in range(1, 10):
        if i-j >= 0:
            dp[i] += dp[i-j]
            dp[i] %= MOD
print(dp[K])
