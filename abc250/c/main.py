N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]
A = list(range(1, N+1))
D = {}
for i in range(N):
    D[i+1] = i

for x in X:
    xi = D[x]
    if xi+1 != N:
        ni = D[A[xi+1]]
    else:
        ni = D[A[xi-1]]
    nv = A[ni]
    A[xi], A[ni] = A[ni], A[xi]
    D[x], D[nv] = ni, xi

print(*A)
