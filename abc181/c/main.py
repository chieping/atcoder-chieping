from itertools import combinations
import sys
readline = sys.stdin.readline

N = int(readline())
points = [tuple(map(int, readline().split())) for _ in range(N)]
ans = False
for P in combinations(points, 3):
    # p3を原点に平行移動する
    # 原点からp1, p2への傾きが一致していればYes
    x1 = P[0][0] - P[2][0]
    y1 = P[0][1] - P[2][1]
    x2 = P[1][0] - P[2][0]
    y2 = P[1][1] - P[2][1]
    ans |= x1 * y2 == x2 * y1 
print('Yes' if ans else 'No')
