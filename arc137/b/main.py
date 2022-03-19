import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
mn, mx, cur, x, y = [0] * 5
for a in [-1 if a == 0 else a for a in A]:
    cur += a
    x = min(x, cur - mx)
    y = max(y, cur - mn)
    mn = min(mn, cur)
    mx = max(mx, cur)
print(y-x+1)
