from itertools import accumulate
N, M = map(int, input().split())
L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l-1)
    R.append(r-1)
S = [0] * (N+1)
for l, r in zip(L, R):
    S[l] += 1
    S[r+1] -= 1
A = list(accumulate(S))
print(A.count(M))
