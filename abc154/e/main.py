# 解説AC
from functools import lru_cache
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
K = int(input())

@lru_cache(maxsize=None)
def f(n, k):
    assert n >= 0
    if n < 10:
        if k == 0:
            return 1
        if k == 1:
            return n
        return 0
    q, r = divmod(n, 10)
    ret = 0
    if k >= 1:
        ret += f(q, k-1) * r
        ret += f(q-1, k-1) * (9-r)
    ret += f(q, k)
    return ret

print(f(N, K))
