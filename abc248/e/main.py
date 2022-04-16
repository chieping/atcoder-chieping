# 解説AC
from collections import defaultdict
from math import gcd
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

if K == 1:
    print('Infinity')
    exit()
cnt = defaultdict(int)
for i, (ax, ay) in enumerate(XY):
    for bx, by in XY[i+1:]:
        dx = ax-bx
        dy = ay-by
        if dx < 0:
            dx = -dx
            dy = -dy
        if dx == 0:
            # xの変化量が0のとき
            dy = 1
        else:
            g = gcd(dx, dy)
            dx //= g
            dy //= g
        a = dx*ay - dy*ax
        # dx,dyの組で傾きを表している
        # aは切片（のようなもの）を表している
        cnt[(dx, dy, a)] += 1

print(sum(v >= K*(K-1)//2 for v in cnt.values()))
