from collections import deque
INF = 10**100

N = int(input())
M = int(input())

maze = [list(input()) for i in range(N)]

sx, sy, gx, gy = -1, -1, -1, -1

for i in range(N):
    if 'S' in maze[i]:
        sy = i
        sx = maze[i].index('S')
    if 'G' in maze[i]:
        gy = i
        gx = maze[i].index('G')

dist = [[INF] * M for i in range(N)]
Q = deque()
Q.append((sy, sx))
dist[sy][sx] = 0

while len(Q) > 0:
    y, x = Q.popleft()
    if x == gx and y == gy:
        break

    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx = x + i
        ny = y + j

        # 移動が可能かの判定とすでに訪れたことがあるかの判定
        if 0 <= nx < N and 0 <= ny < M and maze[ny][nx] != '#' and dist[ny][nx] == INF:
            Q.append((ny, nx))
            dist[ny][nx] = dist[y][x] + 1

# for d in dist: print(*list(map(lambda x: -1 if x == INF else ' ' + str(x) if x < 10 else x, d)))

print(dist[gy][gx])
