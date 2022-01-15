# TLE
from collections import deque
import sys
readline = sys.stdin.readline
H, W = map(int, readline().split())
si, sj = map(int, readline().split())
gi, gj = map(int, readline().split())
G = [['#'] + list(readline()[:-1]) + ['#'] for _ in range(H)]
G.insert(0, ['#'] *(W+2))
G.append(['#'] *(W+2))
dist = [[-1] * (W+2) for _ in range(H+2)]
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
dist[si][sj] = 0

Q = deque()
Q.append((si, sj, 0))
while len(Q) > 0:
    ci, cj, cnt = Q.popleft()
    for dx, dy in d:
        i, j = ci, cj
        while G[i+dx][j+dy] != '#':
            if dist[i+dx][j+dy] == -1:
                Q.append((i+dx, j+dy, cnt+1))
                dist[i+dx][j+dy] = cnt + 1
            i += dx
            j += dy

    if dist[gi][gj] != -1:
        break

print(cnt)
