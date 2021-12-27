# TLE
N, K = map(int, input().split())
x = N
vis = [False] * (10**5)
MOD = 10**5

def f(x):
    _sum = 0
    while x > 0:
        _sum += x % 10
        x //= 10
    return _sum

for i in range(K):
    x = (x + f(x)) % MOD

print(x)
