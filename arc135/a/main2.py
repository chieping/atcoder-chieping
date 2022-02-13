from functools import lru_cache
X = int(input())
MOD = 998244353
@lru_cache
def f(x):
    if x <= 4:
        return x
    return f(x//2) * f((x+1)//2) % MOD
print(f(X))
