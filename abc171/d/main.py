from collections import Counter
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
ans = sum(A)
M = Counter(A)
Q = int(readline())
for _ in range(Q):
    b, c = map(int, readline().split())
    cntB = M[b]
    ans -= b * cntB
    ans += c * cntB
    M[b] = 0
    M[c] += cntB
    print(ans)
