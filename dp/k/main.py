from sys import stdin
N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
# 石の残りがi個のときに、直後の手番の人が勝てるか
dp = [False] * (K+1)
for i in range(K+1):
    for j in range(N):
        dp[i] |= i-A[j] >= 0 and not dp[i-A[j]]
print('First' if dp[K] else 'Second')
