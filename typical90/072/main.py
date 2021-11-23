H, W = map(int, input().split())
C = [[''] * 20 for i in range(20)]
for i in range(1, H+1):
    s = list(input())
    for j in range(1, W+1):
        C[i][j] = s[j-1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
used = [[False]*20 for i in range(20)]

def dfs(sx, sy, px, py):
    if sx == px and sy == py and used[px][py]:
        return 0
    used[px][py] = True

    ret = -10000
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if not (1 <= nx <= H and 1 <= ny <= W and C[nx][ny] == '.'):
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
