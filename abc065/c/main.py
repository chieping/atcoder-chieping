from functools import lru_cache
from math import factorial

N, M = map(int, input().split())
MOD = 10**9 + 7

@lru_cache(maxsize=None)
def fact(n):
    if n - 1 == 0:
        return 1
    return n * factorial(n-1) % MOD

if abs(N-M) > 1:
    print(0)
    exit()

ans = fact(N) * fact(M) % MOD
if N == M:
    ans *= 2
    ans %= MOD
print(ans)
