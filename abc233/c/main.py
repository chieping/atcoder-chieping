from collections import defaultdict
N, X = map(int, input().split())
L = []
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    L.append(a[0])
    A.append(a[1:])
ans = 0

M = defaultdict(int)
M[1] = 1
for i in range(N):
    newM = defaultdict(int)
    for v, cnt in M.items():
        for j in range(L[i]):
            newM[v*A[i][j]] += cnt
    M = newM

print(M[X])
