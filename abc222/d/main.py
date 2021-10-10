N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
P = 998244353
M = 3000
dp = [1] * (M+1)
for i in range(N):
    nx = [0] * (M+1)
    for j in range(A[i], B[i]+1):
        nx[j] = dp[j]
    dp = nx
    for i in range(M):
        dp[i+1] += dp[i]
        dp[i+1] %= P
print(dp[M])

# ナイーブなDP
# dp = [[0] * (M+1) for i in range(N+1)]
# dp[0][0] = 1
# for i in range(1, N+1):
#     for j in range(A[i], B[i]+1):
#         dp[i][j] = sum(dp[i-1][0:j+1]) % P
# ans = 0
# for i in dp[N]:
#     ans += i
#     ans %= P
# print(ans)
