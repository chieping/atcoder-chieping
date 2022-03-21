N = int(input())
T = list(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
d = 0
x = 0
y = 0
for c in T:
    if c == 'S':
        x += dx[d]
        y += dy[d]
    else:
        d = (d + 1) % 4
print(x, y)
