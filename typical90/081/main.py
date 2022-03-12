import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
mx = 5000
# 2次元座標にプロットし、2次元の累積和を計算する
S = [[0]*(mx+1) for _ in range(mx+1)]

for _ in range(N):
    a, b = map(int, readline().split())
    S[a][b] += 1

for i in range(1, mx+1):
    for j in range(1, mx+1):
        S[i][j] += S[i][j-1]

for i in range(1, mx+1):
    for j in range(1, mx+1):
        S[j][i] += S[j-1][i]

ans = 0
for i in range(1, mx-K+1):
    for j in range(1, mx-K+1):
        # 正方形部分に入っている人の数は累積和の足し引きでO(1)で求められる
        res = S[i+K][j+K] - S[i+K][j-1] - S[i-1][j+K] + S[i-1][j-1]
        ans = max(ans, res)

print(ans)
