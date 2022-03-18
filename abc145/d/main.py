X, Y = map(int, input().split())
MOD = 10**9+7

# 移動回数: N
N, r = divmod(X+Y, 3)
if r != 0:
    print(0)
    exit()

# N回の移動のうち、X方向へはXN回、Y方向へはXY回移動する
XN = X - N
XY = Y - N

if 0 > XN or 0 > XY:
    print(0)
    exit()

# ansは N C K
K = XN

fact = [0] * (N+1)
inv = [0] * (N+1)
fact_inv = [0] * (N+1)
fact[0] = 1
fact[1] = 1
fact_inv[0] = 1
fact_inv[1] = 1
inv[1] = 1
for i in range(2, N+1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    fact_inv[i] = fact_inv[i - 1] * inv[i] % MOD

ans = fact[N] * (fact_inv[K] * fact_inv[N-K] % MOD) % MOD
print(ans)
