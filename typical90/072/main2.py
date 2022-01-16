# バックトラック
import sys
readline = sys.stdin.readline
H, W = map(int, readline().split())
C = [['#'] * (W+2) for _ in range(H+2)]
for i in range(1, H+1):
    C[i][1:-1] = list(input())
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
used = [[False]*(W+2) for _ in range(H+2)]

def dfs(sx, sy, px, py):
    if sx == px and sy == py and used[px][py]:
        return 0
    used[px][py] = True
    ret = -10000
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if C[nx][ny] == '#':
            continue
        if (sx != nx or sy != ny) and used[nx][ny]:
            continue
        v = dfs(sx, sy, nx, ny)
        ret = max(ret, v+1)
    used[px][py] = False
    return ret

ans = -1
for i in range(1, H+1):
    for j in range(1, W+1):
        ans = max(ans, dfs(i, j, i, j))

print(ans if ans > 2 else -1)
