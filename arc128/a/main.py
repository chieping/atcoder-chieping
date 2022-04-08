from decimal import Decimal

N = int(input())
A = list(map(Decimal, input().split()))
dp = [[0, 0] for _ in range(N+1)]
dp[0][0] = Decimal(1)
dp[0][1] = Decimal(0)

for i, a in enumerate(A):
    # 金→銀
    dp[i+1][1] = max(dp[i][1], dp[i][0] * a)
    # 銀→金
    dp[i+1][0] = max(dp[i][0], dp[i][1] / a)

ans = []
# dp復元
pos = 0
for i in range(N, 0, -1):
    now = dp[i][pos]
    if dp[i-1][pos] != now:
        pos = abs(pos-1)
        ans.append(1)
    else:
        ans.append(0)

print(*ans[::-1])
