import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
ans = 0
for i in range(N):
    if B[i] > A[i]:
        ans += A[i]
        if i <= N:
            rem = min(A[i+1], B[i] - A[i])
            A[i+1] -= rem
            ans += rem
    else:
        ans += B[i]
print(ans)
