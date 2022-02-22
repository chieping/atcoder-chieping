from collections import deque
import sys
readline = sys.stdin.readline
# すべてのスタート位置を試せばよい

H, W = map(int, readline().split())
S = [list(readline()[:-1]) for _ in range(H)]
D = ((-1,0),(0,-1),(1,0),(0,1))
ans = 0

def bfs(i,j):
    q = deque()
    dist = [[0]*W for _ in range(H)]
    q.append((i,j))
    while len(q)>0:
        x, y = q.popleft()
        for dx, dy in D:
            cx = x+dx
            cy = y+dy
            if 0 <= cx < H and 0 <= cy < W:
                # print(x, dx, y, dy)
                if S[cx][cy] != '#' and dist[cx][cy] == 0 and not (i==cx and j==cy):
                    dist[cx][cy] = dist[x][y]+1
                    q.append((cx, cy))

    return max(max(dist[i]) for i in range(H))            

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        ans = max(ans, bfs(i,j))

print(ans)