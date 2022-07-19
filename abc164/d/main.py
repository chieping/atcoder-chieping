S = list(map(int, input()))
l = len(S)
dp = [0] * 2020
ans = 0
for i, s in enumerate(S, 1):
    prev = dp
    dp = [0] * 2020
    dp[s] = 1
    for j in range(2020):
        dp[(j*10+s)%2019] += prev[j]
    ans += dp[0]
print(ans)
