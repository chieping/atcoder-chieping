from collections import deque
H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
ans = 0
Q = deque()
Q.append([(0, 0)])
visited[0][0] = True
while len(Q) > 0:
    cur = Q.popleft()
    next = []
    for i, j in cur:
        if i + 1 < H and C[i+1][j] == '.' and not visited[i+1][j]:
            next.append((i+1, j))
            visited[i+1][j] = True
        if j + 1 < W and C[i][j+1] == '.' and not visited[i][j+1]:
            next.append((i, j+1))
            visited[i][j+1] = True
    if len(next) > 0:
        Q.append(next)
    ans += 1

print(ans)
