from itertools import product
import sys
readline = sys.stdin.readline

N, M, X = map(int, readline().split())
C = []
A = []
for i in range(N):
    c, *a = map(int, readline().split())
    C.append(c)
    A.append(a)

ans = 10**18
for bits in product([True, False], repeat=N):
    tmp = 0
    L = [0]*M
    idxs = [x for x, bit in zip(range(N), bits) if bit]
    for i in idxs:
        tmp += C[i]
        L = [L[j] + A[i][j] for j in range(M)]
    if min(L) >= X:
        ans = min(ans, tmp)

print(ans if ans != 10**18 else -1)