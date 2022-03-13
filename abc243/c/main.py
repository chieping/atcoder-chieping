from collections import defaultdict
import sys
input = sys.stdin.readline
INF = 10**18
N = int(input())
M = defaultdict(list)
for i in range(N):
    x, y = map(int, input().split())
    M[y].append((x, i))
S = input()[:-1]

for li in M.values():
    li.sort()

    # 右を向いている最も左端の人と
    # 左を向いている最も右端の人が
    # 衝突するかどうかを判定すればよい
    Rmin = INF
    Lmax = -INF
    for x, i in li:
        if S[i] == 'R':
            Rmin = min(Rmin, x)
        if S[i] == 'L':
            Lmax = max(Lmax, x)
    if Rmin < Lmax:
        print('Yes')
        exit()

print('No')