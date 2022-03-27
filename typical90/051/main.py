# 半分全列挙
from bisect import bisect_left
N, K, P = map(int, input().split())
A = list(map(int, input().split()))
A, B = A[:N//2], A[N//2:]

def f(C):
    n = len(C)
    res = [[] for _ in range(n+1)]
    res[0].append(0)
    for a in C:
        for i in range(n-1, -1, -1):
            for s in res[i]:
                res[i+1].append(s+a)
    return res

Ares = f(A)
Bres = f(B)
Ares = [list(sorted(a)) for a in Ares]
Bres = [list(sorted(b)) for b in Bres]

ans = 0

for ai in range(0, len(Ares)):
    bi = K-ai
    if len(Bres) <= bi:
        continue
    for half_sum in Ares[ai]:
        idx = bisect_left(Bres[bi], P-half_sum+1)
        if idx > 0:
            ans += idx
print(ans)
