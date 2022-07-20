from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
C = [[] for _ in range(N+1)]
for i, a in enumerate(A, 1):
    C[a].append(i)
Q = int(input())
for _ in range(Q):
    L, R, X = map(int, input().split())
    ary = C[X]
    # ansはR以下の個数 - L未満の個数
    r = bisect_right(ary, R)
    l = bisect_left(ary, L)
    ans = r - l
    print(ans)
