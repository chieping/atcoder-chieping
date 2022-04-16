from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

B = [[] for _ in range(N+1)]
for i, a in enumerate(A):
    B[a].append(i)

for _ in range(Q):
    l, r, x = map(int, input().split())
    ri = bisect_right(B[x], r-1)
    li = bisect_left(B[x], l-1)
    print(ri-li)
