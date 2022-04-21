from functools import reduce
MOD = 998244353
N, K = map(int, input().split())
CK = [input().split() for _ in range(K)]
P = [0] * N
Q = [False] * N
for i, (c, k) in enumerate(CK):
    k = int(k)-1
    P[k] = 1
    Q[k] = True
    r = range(k+1, N) if c == 'L' else range(k-1, -1, -1)
    for j in r:
        if not Q[j]:
            P[j] += 1
print(reduce(lambda x, y: x*y%MOD, P))
