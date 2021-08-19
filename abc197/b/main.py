H, W, X, Y = map(int, input().split())
S = [input() for i in range(H)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ans = 1

for i in range(4):
    x = X - 1
    y = Y - 1
    while 1:
        x += dx[i]
        y += dy[i]
        if x < 0 or H <= x or y < 0 or W <= y:
            break
        if S[x][y] == '#':
            break
        ans += 1

print(ans)
