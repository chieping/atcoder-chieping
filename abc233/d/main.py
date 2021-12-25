from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
M = defaultdict(int)
ans = 0
latest = 0
M[0] = 1
for a in A:
    latest += a
    ans += M[latest-K]
    M[latest] += 1
print(ans)
