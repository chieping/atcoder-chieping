from bisect import bisect_left, bisect_right
from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

D = defaultdict(int)
B = [[] for _ in range(N+1)]
for i, a in enumerate(A):
    D[a] += 1
    B[a].append(i)

for _ in range(Q):
    l, r, x = map(int, input().split())
    # print(D[r][x] - D[l-1][x])
    ans = D[x]
    ri = bisect_right(B[x], r-1)
    ans -= (len(B[x])-ri)
    li = bisect_left(B[x], l-1)
    ans -= li
    print(ans)


