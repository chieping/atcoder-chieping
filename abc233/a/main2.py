from math import ceil, floor
from sys import stdin
X, Y = map(int, stdin.readline().split())
ans = max(0, ceil((Y-X)/10))
print(ans)
