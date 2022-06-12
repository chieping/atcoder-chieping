x, y, W = input().split()
x = int(x)-1
y = int(y)-1
C = [list(map(int, input())) for _ in range(9)]

dx = 0
dy = 0
if 'R' in W:
    dx += 1
if 'L' in W:
    dx -= 1
if 'U' in W:
    dy -= 1
if 'D' in W:
    dy += 1

ans = []
for i in range(4):
    if x + (dx*i) <= 8:
        cx = abs(x + (dx*i))
    else:
        cx = 16 - (x + (dx*i))
    if y + (dy*i) <= 8:
        cy = abs(y + (dy*i))
    else:
        cy = 16 - (y + (dy*i))
    ans.append(C[cy][cx])
print(*ans, sep='')
