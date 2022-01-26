from bisect import bisect_left
import sys
readline = sys.stdin.readline
X, N = map(int, readline().split())
P = set(map(int, readline().split()))

PP = []
for i in range(-1, 102):
    if i not in P:
        PP.append(i)

idx = bisect_left(PP, X)
a = PP[idx-1]
b = PP[idx]
if abs(a-X) <= abs(b-X):
    print(a)
else:
    print(b)
