import sys
readline = sys.stdin.readline
N = int(readline())
A = sorted(map(int, readline().split()), reverse=True)
ans = -A[0]
for i in range(N):
    ans += A[i//2]
print(ans)