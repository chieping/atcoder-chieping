from functools import lru_cache
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, K = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
MOD = 10**9+7

ans = 1

@lru_cache(maxsize=10000)
def mod_fact(x):
    ret = 1
    for i in range(1, x+1):
        ret *= i
        ret %= MOD
    return ret

@lru_cache(maxsize=10000)
def mod_pow(x, a):
    return pow(x, a, MOD)

@lru_cache(maxsize=10000)
def permutation(n, k):
    if n < 0 or n < k:
        return 0
    inv = mod_pow(mod_fact(n-k), MOD-2)
    return mod_fact(n) * inv % MOD

def dfs(v, p=-1):
    global ans
    for u in edge[v]:
        if u == p:
            continue
        dfs(u, v)
    nk = K if p == -1 else K - 2
    c = len(edge[v]) + 1 if p == -1 else len(edge[v]) - 1
    ans *= permutation(nk, c)
    ans %= MOD

dfs(0)
print(ans)