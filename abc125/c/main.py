from math import gcd
N = int(input())
A = list(map(int, input().split()))
L = [0] * N
R = [0] * N
L[0] = A[0]
for i in range(1, N):
    L[i] = gcd(L[i-1], A[i])
R[-1] = A[-1]
for i in range(N-2, -1, -1):
    R[i] = gcd(R[i+1], A[i])
ans = 0
for i in range(N):
    l = L[i-1] if i-1 >= 0 else 0
    r = R[i+1] if i+1 < N else 0
    ans = max(ans, gcd(l, r))
print(ans)
