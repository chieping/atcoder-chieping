import sys
readline = sys.stdin.readline
N = int(readline())
S = [list(readline()[:-1]) for _ in range(N)]
DX = [0, 1, 1, 1]
DY = [1, 0, 1, -1]

def f(i, j, dx, dy):
    x = i
    y = j
    b = 0
    r = 2
    while r >= 0 and 0 <= y < N and 0 <= x < N:
        if S[x][y] == '#':
            b += 1
        else:
            b += 1
            r -= 1
        if b == 6 and r >= 0:
            return True
        x += dx
        y += dy
    return False

for i in range(N):
    for j in range(N):
        for k in range(4):
            if f(i, j, DX[k], DY[k]):
                print('Yes')
                exit()
print('No')