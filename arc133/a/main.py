import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))

succ = 0
for i in range(N):
    if succ > A[i]:
        remove = succ
        break
    succ = A[i]
else:
    remove = A[-1]

A = [x for x in A if x != remove]
print(*A)
