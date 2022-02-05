import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
B = [0, 360]
c = 0
for i in range(N):
    c = (c+A[i]) % 360
    B.append(c)
B.sort()
ans = 0
for i in range(len(B)-1):
    ans = max(ans, B[i+1]-B[i])
print(ans)