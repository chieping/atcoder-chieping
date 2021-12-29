from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
A.sort()

ans = 0
sub = 0
for i in range(1, N):
    sub += A[i-1]
    ans += A[i]*i-sub

print(ans)

