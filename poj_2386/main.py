N, M = map(int, input().split())
data = [list(input()) for i in range(N)]

def dfs(x, y):
    data[x][y] = '.'
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 'W':
                dfs(nx, ny)

ans = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 'W':
            dfs(i, j)
            ans += 1

print(ans)
