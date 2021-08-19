H, W, X, Y = map(int, input().split())
x = X - 1
y = Y - 1

S = [input() for i in range(H)]

ans = 1

x -= 1
while x >= 0:
    if S[x][y] == '.':
        ans += 1
    else:
        break
    x -= 1
x = X
while x < H:
    if S[x][y] == '.':
        ans += 1
    else:
        break
    x += 1
x = X - 1
y -= 1
while y >= 0:
    if S[x][y] == '.':
        ans += 1
    else:
        break
    y -= 1
y = Y
while y < W:
    if S[x][y] == '.':
        ans += 1
    else:
        break
    y += 1

print(ans)
