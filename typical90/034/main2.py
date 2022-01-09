from collections import defaultdict
import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
A = list(map(int, readline().split()))

C = defaultdict(int)
cnt = 0
ans = 0
r = 0
for l in range(N):
    while cnt <= K:
        ans = max(ans, r-l)
        if r >= N:
            break
        if C[A[r]] == 0:
            cnt += 1
        C[A[r]] += 1
        r += 1
    if C[A[l]] == 1:
        cnt -= 1
    C[A[l]] -= 1

print(ans)
