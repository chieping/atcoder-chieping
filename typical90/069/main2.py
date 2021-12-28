from sys import stdin
N, K = map(int, stdin.readline().split())
MOD = 10**9+7

# 繰り返し二乗法
def pow(x, y):
    if y == 0:
        return 1
    if y % 2 == 1:
        return x * pow(x, y-1) % MOD
    a = pow(x, y//2)
    return a**2 % MOD

ans = K
if N > 1:
    ans *= (K-1)
    ans = ans * pow(K-2, N-2) % MOD
print(ans)
