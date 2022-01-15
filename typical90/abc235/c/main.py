from collections import defaultdict
import sys
readline = sys.stdin.readline
N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

M = defaultdict(list)
for i in range(N):
    M[A[i]].append(i+1)

for _ in range(Q):
    x, k = map(int, readline().split())
    if len(M[x]) < k:
        print(-1)
    else:
        print(M[x][k-1])
