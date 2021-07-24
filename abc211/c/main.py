MOD = 1_000_000_007
s = input()
n = len(s)
cho = 'chokudai'

dp = [0] * (len(cho) + 1)
dp[0] = 1

for i in range(n):
    for j in range(len(cho)):
        if s[i] == cho[j]:
            dp[j+1] = (dp[j+1] + dp[j]) % MOD

print(dp[8])
