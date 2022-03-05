MOD = 998244353
N = int(input())

# 最後の桁がiで終わる組み合わせの数
dp = [1] * 11

for _ in range(N-1):
    prev = dp
    dp = [0] * 11
    
    for i in range(1,10):
        dp[i-1] += prev[i]
        dp[i] += prev[i]
        dp[i+1] += prev[i]
    for i in range(1, 10):
        dp[i] %= MOD

print(sum(dp[1:10]) % MOD)
