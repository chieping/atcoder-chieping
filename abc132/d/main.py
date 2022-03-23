# 解説AC
N, K = map(int, input().split())
MOD = 10**9+7
# パスカルの三角形
C = [[0] * 4005 for _ in range(4005)]
C[0][0] = 1
for i in range(4000+1):
    for j in range(i+1):
        C[i+1][j] = (C[i+1][j] + C[i][j]) % MOD
        C[i+1][j+1] = (C[i+1][j+1] + C[i][j]) % MOD

def f2(n, k):
    return C[n+k-1][k-1]

def f(n, k):
    if n < k: return 0
    if n == 0 and k == 0: return 1
    if k < 1: return 0
    return f2(n-k, k)

for i in range(1, K+1):
    blue = f(K, i)
    red = 0
    red += f(N-K, i-1)
    red += f(N-K, i)
    red += f(N-K, i)
    red += f(N-K, i+1)
    ans = blue*red%MOD
    print(ans)
