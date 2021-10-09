N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
P = 998244353
ans = 1

bp = 0
for i in range(N):
    if A[i] > bp:
        ans *= (2*((bp -1)+A[i])) // (bp-A[i])
    ans *= ((B[i]-max(A[i], bp)))
    ans %= P
    bp = B[i]

print(ans)

